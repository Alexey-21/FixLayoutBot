import telebot
from collections import namedtuple
from telebot import types
import sqlite3
from datetime import datetime
bot = telebot.TeleBot("8468360526:AAFbp5OfBIsw4nU6YNdmZVLnD1TcHcrcTEw", parse_mode='HTML')
strelka = u"\U000027A1"
opat_tonkosti = 0
ispr_str = ''
user_states = {}


def init_db():
    conn = sqlite3.connect('bot_stats.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY, 
                first_seen TEXT,
                last_seen TEXT)''')
    conn.commit()
    conn.close()

init_db()


def update_stats(user_id):
    conn = sqlite3.connect('bot_stats.db')
    c = conn.cursor()
    now = datetime.now().isoformat()

    c.execute("SELECT 1 FROM users WHERE user_id=?", (user_id,))
    exists = c.fetchone()

    if exists:
        c.execute("UPDATE users SET last_seen=? WHERE user_id=?", (now, user_id))
    else:
        c.execute("INSERT INTO users (user_id, first_seen, last_seen) VALUES (?, ?, ?)",
                  (user_id, now, now))
    conn.commit()
    conn.close()


def get_stats():
    conn = sqlite3.connect('bot_stats.db')
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM users")
    total_users = c.fetchone()[0]

    today = datetime.now().date().isoformat()
    c.execute("SELECT COUNT(*) FROM users WHERE DATE(last_seen) = ?", (today,))
    daily_users = c.fetchone()[0]

    conn.close()
    return total_users, daily_users


Pair = namedtuple('Pair', ['first', 'second'])
pair_1 = Pair('q', 'й')
pair_2 = Pair('w', 'ц')
pair_3 = Pair('e', 'у')
pair_4 = Pair('r', 'к')
pair_5 = Pair('t', 'е')
pair_6 = Pair('y', 'н')
pair_7 = Pair('u', 'г')
pair_8 = Pair('i', 'ш')
pair_9 = Pair('o', 'щ')
pair_10 = Pair('p', 'з')
pair_11 = Pair('[', 'х')
pair_12 = Pair(']', 'ъ')
pair_13 = Pair('a', 'ф')
pair_14 = Pair('s', 'ы')
pair_15 = Pair('d', 'в')
pair_16 = Pair('f', 'а')
pair_17 = Pair('g', 'п')
pair_18 = Pair('h', 'р')
pair_19 = Pair('j', 'о')
pair_20 = Pair('k', 'л')
pair_21 = Pair('l', 'д')
pair_22 = Pair(';', 'ж')
pair_23 = Pair('', 'э')
pair_24 = Pair('z', 'я')
pair_25 = Pair('x', 'ч')
pair_26 = Pair('c', 'с')
pair_27 = Pair('v', 'м')
pair_28 = Pair('b', 'и')
pair_29 = Pair('n', 'т')
pair_30 = Pair('m', 'ь')
pair_31 = Pair(',', 'б')
pair_32 = Pair('.', 'ю')
pair_33 = Pair('/', '.')
pair_34 = Pair('`', 'ё')
pair_35 = Pair('|', '/')
pair_36 = Pair('~', 'Ё')
pair_37 = Pair('Q', 'Й')
pair_38 = Pair('W', 'Ц')
pair_39 = Pair('E', 'У')
pair_40 = Pair('R', 'К')
pair_41 = Pair('T', 'Е')
pair_42 = Pair('Y', 'Н')
pair_43 = Pair('U', 'Г')
pair_44 = Pair('I', 'Ш')
pair_45 = Pair('O', 'Щ')
pair_46 = Pair('P', 'З')
pair_47 = Pair('{', 'Х')
pair_48 = Pair('}', 'Ъ')
pair_49 = Pair('A', 'Ф')
pair_50 = Pair('S', 'Ы')
pair_51 = Pair('D', 'В')
pair_52 = Pair('F', 'А')
pair_53 = Pair('G', 'П')
pair_54 = Pair('H', 'Р')
pair_55 = Pair('J', 'О')
pair_56 = Pair('K', 'Л')
pair_57 = Pair('L', 'Д')
pair_58 = Pair(':', 'Ж')
pair_59 = Pair('"', 'Э')
pair_60 = Pair('Z', 'Я')
pair_61 = Pair('X', 'Ч')
pair_62 = Pair('C', 'С')
pair_63 = Pair('V', 'М')
pair_64 = Pair('B', 'И')
pair_65 = Pair('N', 'Т')
pair_66 = Pair('M', 'Ь')
pair_67 = Pair('<', 'Б')
pair_68 = Pair('>', 'Ю')
pair_69 = Pair('?', ',')
pair_70 = Pair(' ', ' ')

pair_raskladok = [pair_1, pair_2, pair_3, pair_4, pair_5, pair_6, pair_7, pair_8, pair_9, pair_10, pair_11, pair_12, pair_13, pair_14, pair_15, pair_16, pair_17, pair_18, pair_19, pair_20, pair_21, pair_22, pair_23, pair_24, pair_25, pair_26 ,pair_27, pair_28, pair_29, pair_30, pair_31, pair_32, pair_33, pair_34, pair_35, pair_36, pair_37, pair_38, pair_39, pair_40, pair_41, pair_42, pair_43, pair_44, pair_45, pair_46, pair_47, pair_48, pair_49, pair_50, pair_51, pair_52, pair_53, pair_54, pair_55, pair_56, pair_57, pair_58, pair_59, pair_60, pair_61, pair_62, pair_63, pair_64, pair_65, pair_66, pair_67, pair_68, pair_69, pair_70]

def start_markup():
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text = f'Рус {strelka} Англ', callback_data='start_ru_angl')
    btn_2 = types.InlineKeyboardButton(text = f'Англ {strelka} Рус', callback_data='start_angl_ru')
    markup.add(btn_1, btn_2)
    return markup

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    update_stats(user_id)
    bot.send_message(message.chat.id, 'Этот бот поможет тебе исправить раскладку сообщения.\n\nТебя ведь тоже раздражает, когда забываешь переключить раскладку и пишешь "ghbdtn" вместо "привет"?\n\nТогда просто перешли сообщение этому боту и получи исправленный тект. Чтобы начать напиши /fix.')

@bot.message_handler(commands=['fix'])
def fix_message(message):
    user_id = message.from_user.id
    update_stats(user_id)
    bot.send_message(message.chat.id,'Выбери с какой раскалдки на какую исправить текст.',reply_markup=start_markup())

@bot.message_handler(commands=['stats'])
def send_stats(message):
    total, daily = get_stats()
    bot.reply_to(message,
        f"📊 Статистика бота:\n"
        f"• Всего пользователей: {total}\n"
        f"• Сегодня активных: {daily}"
    )

@bot.callback_query_handler(func= lambda call:call.data.startswith)
def check_click_message(call):
        if call.data == 'start_ru_angl':
            global tumb
            tumb = 'start_ru_angl'
            bot.send_message(call.message.chat.id, 'Отлично, теперь пришли боту сообщение, которое нужно исправить.')
        if call.data == 'start_angl_ru':
            tumb = 'start_angl_ru'
            bot.send_message(call.message.chat.id, 'Отлично, теперь пришли боту сообщение, которое нужно исправить.')
@bot.message_handler(content_types=['text'])
def check_click_one(message):
    user_id = message.from_user.id
    update_stats(user_id)
    global ispr_str
    global eror_1
    eror_1 = 'no'
    global eror_2
    eror_2 = 'no'
    if tumb == 'start_ru_angl':
        global fix_rask
        fix_rask = str(message.text)
        n = len(fix_rask)
        symbol_num = ''
        i = 0
        for i in range(0, n, 1):
            if fix_rask[i] == ' ':
                ispr_str += ' '
            else:
                for j in range(0, 69, 1):
                    pair_now = pair_raskladok[j]
                    if pair_now.second == fix_rask[i]:
                        symbol_num = j
                if symbol_num == None:
                    bot.send_message(message.chat.id, 'Ты выбрал перевод с русской раскладки на английскую, а написал сообщение на английском, а не на русском.\n\nЕсли тебе нужно перевести сообщение с английской раскладки на русскую, то напиши /fix и выбери этот вариант')
                    eror_1 = 'yes'
                    break
                else:
                    pair_after = pair_raskladok[symbol_num]
                    ispr_str += pair_after.first
    elif tumb == 'start_angl_ru':
        fix_rask = str(message.text)
        m = len(fix_rask)
        symbol_num_2 = ''
        i = 0
        for i in range(0, m, 1):
            if fix_rask[i] == ' ':
                ispr_str += ' '
            else:
                for j in range(0, 69, 1):
                    pair_now = pair_raskladok[j]
                    if pair_now.first == fix_rask[i]:
                        symbol_num_2 = j
                if symbol_num_2 == '':
                    bot.send_message(message.chat.id, 'Ты выбрал перевод с английской раскладки на русскую, а написал сообщение на русском, а не на английском.\n\nЕсли тебе нужно перевести сообщение с русской раскладки на английскую, то напиши /fix и выбери этот вариант')
                    eror_2 = 'yes'
                    break
                else:
                    pair_after = pair_raskladok[symbol_num_2]
                    ispr_str += pair_after.second
    else:
        global opat_tonkosti
        opat_tonkosti = 1
        bot.send_message(message.chat.id, 'Выбери с какой раскалдки на какую исправить текст.',
                         reply_markup=start_markup())
    if opat_tonkosti != 1:
        if eror_1 == 'no' and eror_2 == 'no':
            ispr_soob = 'Исправленное сообщение(нажми на него, чтобы копировать):\n\n`' + str(ispr_str) + '`\n\nЧтобы исправить ещё одно сообщение просто пришли его этому боту.\n\nЧтобы вернуться в меню выбора раскладки напиши /fix.'
            bot.send_message(message.chat.id, ispr_soob, parse_mode="MARKDOWN")
            ispr_str = ''
            bot.delete_message(message.chat.id, message.message_id - 1)
            bot.delete_message(message.chat.id, message.message_id - 2)

bot.polling(none_stop=True)