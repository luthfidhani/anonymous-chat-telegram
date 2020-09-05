m_start = '\n🤖 Hay.. Anda berada dalam obrolan anonim!\n'

m_is_not_free_users = '🤖 Mencari yang cocok...'\

m_is_connect = '🤖 Partner ditemukan, say "Hay \U0001F44B"'\

m_play_again = '🤖 Ingin mengobrol dengan orang lain?'

m_is_not_user_name = '🤖 Maaf, tetapi di bot kami, komunikasi hanya dapat dilakukan jika Anda memiliki nama pengguna'

m_good_bye = '🤖 Bot berhenti, klik Mulai untuk memulai kembali'

m_disconnect_user = '🤖 ouch..! Dia pergi'

m_failed = '🤖 Telah terjadi kesalahan!'

m_like = '🤖 Pilihan bagus!'

m_dislike_user = '🤖 Dialog berakhir'

m_dislike_user_to = '🤖 Teman bicara tidak menyukaimu, maaf'

m_send_some_messages = '🤖 Anda tidak dapat meneruskan pesan Anda sendiri'

m_has_not_dialog = '🤖 Anda tidak dalam dialog'

m_success_sharelink = '🤖 Profile mu sudah terkirim'

m_help = ' 🤖 <b>Bot Bantuan</b> 🤖\n\n'\
    '\U000025B6 <b>Mulai Bot = </b> <code>untuk memulai bot</code>\n\n'\
    '\U0001F50D <b>Cari Partner = </b> <code>Mencari partner</code>\n\n'\
    '\U000023E9 <b>Next = </b> <code>Menghentikan dialog dan mencari partner baru</code>\n\n'\
    '\U000026D4 <b>Berhenti = </b> <code>Menghentikan dialog</code>\n\n'\
    '🤝 <b>Share Profile = </b> <code>mengirimkan username Telegram ke partner</code>\n\n'\
    '\U0001F4BB <b>Bantuan = </b> <code>Cara menggunakan bot</code>\n\n'\
    '\U0001F6A7 <b>Syarat & Ketentuan = </b> <code>Aturan penggunaan bot</code>\n\n'\

m_terms = '🤖 Untuk penggunaan Bot ini, anda dapat mengakses <a href="https://www.w3schools.com">DISINI!</a> '

stop_str = '\U000026D4 Berhenti'

new_str = '\U00002709 New Chat'

skip_str = '\U000023E9 Next'

search_str = '\U0001F50D Cari Partner'

sharelink_str = '🤝 Share Profile'

terms_str = '\U0001F6A7 Syarat & Ketentuan'

help_str = '\U0001F4BB Bantuan'

start_str = '\U000025B6 Mulai Bot'

def m_sharelink(x):
    return ('🤖 Hai.. kamu dapat profile partner kamu loh \n Nama usernamenya @' + str(x) + '\n')