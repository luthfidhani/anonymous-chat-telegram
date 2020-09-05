import telebot
from telebot import types

from Messages import *
from dataEgine import *


access_token = '862074484:AAELO0aDqSEq7g9NU1mN9J-nZCC5FofDW70'
bot = telebot.TeleBot(access_token)

# Button 

def button_start():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add(search_str)
    markup.add(stop_str)
    markup.add(help_str)
    markup.add(terms_str)
    return markup

# function

def stop(message):
    remove = types.ReplyKeyboardRemove()
    user_id = message.chat.id
    
    if message.chat.id in communications:
        user_to_id = communications[user_id]['UserTo']
        # bot.send_message(user_to_id, m_disconnect_user, reply_markup=new_stop())

        delete_info(user_to_id)

    delete_user_from_db(user_id)

    bot.send_message(user_id, m_good_bye, reply_markup=stop_str)

# request

@bot.message_handler(commands=['start'])
def echo(message):
    message.chat.type = 'private'
    self_id = message.chat.id

    if message.chat.username is None:
        bot.send_message(self_id, m_is_not_user_name)
        return

    bot.send_message(self_id, m_start, reply_markup=button_start())

@bot.message_handler(func=lambda call: call.text == stop_str)
def echo(message):
    stop(message)
    


if __name__ == '__main__':
    recovery_data()
    bot.stop_polling()
    bot.polling(none_stop=True)
