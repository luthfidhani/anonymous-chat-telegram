import telebot
from telebot import types
import telegram

from Messages import *
from dataEgine import *


access_token = '862074484:AAELO0aDqSEq7g9NU1mN9J-nZCC5FofDW70'
bot = telebot.TeleBot(access_token)

# ================== BUTTON AREA =====================

def inline_menu():
    callback = types.InlineKeyboardButton(text='\U00002709 New chat', callback_data='NewChat')
    menu = types.InlineKeyboardMarkup()
    menu.add(callback)

    return menu

def button_start():
    types.ReplyKeyboardRemove()

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add(search_str)
    markup.add(stop_str)
    markup.add(help_str)
    markup.add(terms_str)
    return markup

def skip_stop():
    types.ReplyKeyboardRemove()

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add(skip_str)
    markup.add(stop_str)
    markup.add(sharelink_str)

    return markup

def search_stop():
    types.ReplyKeyboardRemove()

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add(search_str)
    markup.add(stop_str)

    return markup

# ================== FUNCTION AREA =====================

def connect_user(user_id):
    if user_id in communications:
        return True
    else:
        bot.send_message(user_id, m_has_not_dialog)
        return False

def start(message):
    message.chat.type = 'private'
    self_id = message.chat.id

    if message.chat.username is None:
        bot.send_message(self_id, m_is_not_user_name)
        return

    bot.send_message(self_id, m_start, reply_markup=button_start())
    # bot.send_message(self_id, m_start)

def search(call):
    user_id = call.chat.id
    user_to_id = None

    add_users(chat=call.chat)

    def button():
        types.ReplyKeyboardRemove()
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
        markup.add(stop_str)
        return markup


    if len(free_users) < 2:
        bot.send_message(user_id, m_is_not_free_users, reply_markup=button())
        return

    if free_users[user_id]['state'] == 0:
        return

    for user in free_users:
        if user['state'] == 0:
            user_to_id = user['ID']
            break

    if user_to_id is None:
        bot.send_message(user_id, m_is_not_free_users, reply_markup=button())
        return

    add_communications(user_id, user_to_id)

    bot.send_message(user_id, m_is_connect, reply_markup=skip_stop())
    bot.send_message(user_to_id, m_is_connect, reply_markup=skip_stop())

def stop(message):
    remove = types.ReplyKeyboardRemove()
    user_id = message.chat.id

    def button():
        types.ReplyKeyboardRemove()
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
        markup.add(start_str)
        return markup
    
    if message.chat.id in communications:
        user_to_id = communications[user_id]['UserTo']
        bot.send_message(user_to_id, m_disconnect_user, reply_markup=search_stop())
        

        delete_info(user_to_id)

    delete_user_from_db(user_id)

    bot.send_message(user_id, m_good_bye, reply_markup=button())
    # bot.send_message(user_id, "", reply_markup=remove)

def skip(message):
    user_id = message.chat.id
    if user_id not in communications:
        bot.send_message(user_id, m_failed)
        return
    else:
        user_to_id = communications[user_id]['UserTo']

        bot.send_message(user_id, m_dislike_user, reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(user_to_id, m_disconnect_user, reply_markup=types.ReplyKeyboardRemove())

        delete_info(user_to_id)
        bot.send_message(user_to_id, m_play_again, reply_markup=search_stop())

        search(message)

def helps(message):
    user_id = message.chat.id
    bot.send_message(user_id, m_help, parse_mode=telegram.ParseMode.HTML)

def terms(message):
    user_id = message.chat.id
    bot.send_message(user_id, m_terms, parse_mode=telegram.ParseMode.HTML)

def sharelink(message):
    user_id = message.chat.id
    user_name = message.chat.username
    if user_id not in communications:
        bot.send_message(user_id, m_failed)
        return
    else:
        user_to_id = communications[user_id]['UserTo']
        bot.send_message(user_to_id, m_sharelink(user_name))
        bot.send_message(user_id, m_success_sharelink)


# ================== REQUEST AREA =====================

@bot.message_handler(commands=['start'])
def echo(message):
    start(message)

@bot.message_handler(commands=['search'])
def echo(call):
    search(call)

@bot.message_handler(commands=['skip'])
def echo(message):
    skip(message)

@bot.message_handler(commands=['stop'])
def echo(message):
    stop(message)

@bot.message_handler(commands=['help'])
def echo(message):
    helps(message)

@bot.message_handler(commands=['terms'])
def echo(message):
    terms(message)

@bot.message_handler(commands=['sharelink'])
def echo(message):
    sharelink(message)

@bot.message_handler(func=lambda call: call.text == start_str)
def echo(message):
    start(message)

@bot.message_handler(func=lambda call: call.text == search_str)
def echo(message):
    search(message)

@bot.message_handler(func=lambda call: call.text == skip_str)
def echo(message):
    skip(message)

@bot.message_handler(func=lambda call: call.text == stop_str)
def echo(message):
    stop(message)

@bot.message_handler(func=lambda call: call.text == help_str)
def echo(message):
    helps(message)

@bot.message_handler(func=lambda call: call.text == terms_str)
def echo(message):
    terms(message)

@bot.message_handler(func=lambda call: call.text == sharelink_str)
def echo(message):
    sharelink(message)

@bot.message_handler(content_types=['text', 'sticker', 'video', 'photo', 'audio', 'voice'])
def echo(message):
    """
    Resend message to anonymous friend.
    :param message:
    :return:
    """
    user_id = message.chat.id
    if message.content_type == 'sticker':
        if not connect_user(user_id):
            return

        bot.send_sticker(communications[user_id]['UserTo'], message.sticker.file_id)

    elif message.content_type == 'photo':
        if not connect_user(user_id):
            return

        file_id = None

        for item in message.photo:
            file_id = item.file_id

        bot.send_photo(communications[user_id]['UserTo'],file_id, caption=message.caption)

    elif message.content_type == 'audio':
        if not connect_user(user_id):
            return

        bot.send_audio(communications[user_id]['UserTo'],message.audio.file_id, caption=message.caption)
    
    elif message.content_type == 'video':
        if not connect_user(user_id):
            return

        bot.send_video(communications[user_id]['UserTo'],message.video.file_id, caption=message.caption)
    
    elif message.content_type == 'voice':
        if not connect_user(user_id):
            return

        bot.send_voice(communications[user_id]['UserTo'], message.voice.file_id)

    elif message.content_type == 'text':
        if message.text != '/start' and message.text != '/stop' and message.text != stop_str and message.text != skip_str and message.text != 'NewChat':

            if not connect_user(user_id):
                return

            if message.reply_to_message is None:
                bot.send_message(communications[user_id]['UserTo'], message.text)

            elif message.from_user.id != message.reply_to_message.from_user.id:
                print(message.reply_to_message.message_id)
                bot.send_message(communications[user_id]['UserTo'], message.text, reply_to_message_id=message.reply_to_message.message_id - 1)
            
            else:
                print(message.reply_to_message.message_id)
                bot.send_message(communications[user_id]['UserTo'], message.text, reply_to_message_id=message.reply_to_message.message_id + 1)



@bot.callback_query_handler(func=lambda call: True)
def echo(call):
    """
    Create new chat.
    All users are divided into two categories: receivers and emitters.
    If bot finds pair, then it creates new chat.
    :param call:
    :return:
    """
    
    if call.data == 'NewChat':
        user_id = call.message.chat.id
        user_to_id = None

        print(call.message.chat)
        add_users(chat=call.message.chat)

        if len(free_users) < 2:
            bot.send_message(user_id, m_is_not_free_users)
            return

        if free_users[user_id]['state'] == 0:
            return

        for user in free_users:
            if user['state'] == 0:
                user_to_id = user['ID']
                break

        if user_to_id is None:
            bot.send_message(user_id, m_is_not_free_users)
            return

        keyboard = skip_stop()

        add_communications(user_id, user_to_id)

        bot.send_message(user_id, m_is_connect, reply_markup=keyboard)
        bot.send_message(user_to_id, m_is_connect, reply_markup=keyboard)


if __name__ == '__main__':
    recovery_data()
    bot.stop_polling()
    bot.polling(none_stop=True)
