import datetime
import psycopg2
import telebot
from telebot import types
from math import ceil

bot = telebot.TeleBot('2139251123:AAFppLy0Imoq7p-CILZUukFVP_0vGPZT0WI')

week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Субботу', 'Воскресенье']
d1 = datetime.datetime.strptime("01-09-2021", "%d-%m-%Y")
d2 = datetime.datetime.strptime(str(datetime.datetime.date(datetime.datetime.now())), "%Y-%m-%d")
d = ceil(((d2 - d1).days + 3) / 7)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать работу')
    markup.add(btn1)
    bot.send_message(message.chat.id, "Привет", reply_markup=markup)


@bot.message_handler(content_types='text')
def reply_message(message):
    conn = psycopg2.connect(database="t_t", user="postgres", password="ag12122002", host="localhost", port="5432")
    cursor = conn.cursor()
    if message.text == "Начать работу":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Расписание на сегодня')
        btn2 = types.KeyboardButton('Расписание на завтра')
        btn3 = types.KeyboardButton('Расписание')
        btn4 = types.KeyboardButton('Помощь')
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        bot.send_message(message.chat.id, "Выберете действие", reply_markup=markup)
    if message.text == "Расписание на сегодня":
        if datetime.datetime.weekday(datetime.datetime.now()) < 5:
            if d % 2 > 0:
                cursor.execute("SELECT subject, start_time FROM time_table WHERE day='" + week[
                    datetime.datetime.weekday(datetime.datetime.now())] + "' and (pos = 'в' or pos = '-');")
                row = list(cursor.fetchall())
                mess = ''
                for i in row:
                    mess += str(i[0]) + ' '
                    mess += str(i[1]) + '\n'
                bot.send_message(message.chat.id, mess)
                conn.close()
            else:
                cursor.execute("SELECT subject, start_time FROM time_table WHERE day='" + week[
                    datetime.datetime.weekday(datetime.datetime.now())] + "' and (pos = 'н' or pos = '-');")
                row = list(cursor.fetchall())
                mess = ''
                for i in row:
                    mess += str(i[0]) + ' '
                    mess += str(i[1]) + '\n'
                bot.send_message(message.chat.id, mess)
                conn.close()
        else:
            bot.send_message(message.chat.id,
                             "В " + week[datetime.datetime.weekday(datetime.datetime.now())] + " не учимся!")
    if message.text == "Расписание на завтра":
        if datetime.datetime.weekday(datetime.datetime.now()) < 4:
            if d % 2 > 0:
                cursor.execute("SELECT subject, start_time FROM time_table WHERE day='" + week[
                    datetime.datetime.weekday(datetime.datetime.now()) + 1] + "' and (pos = 'в' or pos = '-');")
                row = list(cursor.fetchall())
                mess = ''
                for i in row:
                    mess += str(i[0]) + ' '
                    mess += str(i[1]) + '\n'
                bot.send_message(message.chat.id, mess)
                conn.close()
            else:
                cursor.execute("SELECT subject, start_time FROM time_table WHERE day='" + week[
                    datetime.datetime.weekday(datetime.datetime.now()) + 1] + "' and (pos = 'н' or pos = '-');")
                row = list(cursor.fetchall())
                mess = ''
                for i in row:
                    mess += str(i[0]) + ' '
                    mess += str(i[1]) + '\n'
                bot.send_message(message.chat.id, mess)
                conn.close()
        else:
            bot.send_message(message.chat.id,
                             "В " + (week[datetime.datetime.weekday(datetime.datetime.now()) + 1]) + " не учимся!")
    if message.text == "Расписание":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Понедельник')
        btn2 = types.KeyboardButton('Вторник')
        btn3 = types.KeyboardButton('Среда')
        btn4 = types.KeyboardButton('Четверг')
        btn5 = types.KeyboardButton('Пятница')
        btn6 = types.KeyboardButton('Назад')
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn5)
        markup.add(btn6)
        bot.send_message(message.chat.id, "Выберете день недели", reply_markup=markup)
    if message.text == "Понедельник":
        if d % 2 > 0:
            cursor.execute("SELECT subject, start_time FROM time_table WHERE day = 'Пн' and (pos = 'в' or pos = '-');")
            row = list(cursor.fetchall())
            mess = ''
            for i in row:
                mess += str(i[0]) + ' '
                mess += str(i[1]) + '\n '
            bot.send_message(message.chat.id, mess)
            conn.close()
        else:
            cursor.execute("SELECT subject, start_time FROM time_table WHERE day = 'Пн' and (pos = 'н' or pos = '-');")
            row = list(cursor.fetchall())
            mess = ''
            for i in row:
                mess += str(i[0]) + ' '
                mess += str(i[1]) + '\n'
            bot.send_message(message.chat.id, mess)
            conn.close()
    if message.text == "Вторник":
        if d % 2 > 0:
            cursor.execute("SELECT subject, start_time FROM time_table WHERE day = 'Вт' and (pos = 'в' or pos = '-');")
            row = list(cursor.fetchall())
            mess = ''
            for i in row:
                mess += str(i[0]) + ' '
                mess += str(i[1]) + '\n '
            bot.send_message(message.chat.id, mess)
            conn.close()
        else:
            cursor.execute("SELECT subject, start_time FROM time_table WHERE day = 'Вт' and (pos = 'н' or pos = '-');")
            row = list(cursor.fetchall())
            mess = ''
            for i in row:
                mess += str(i[0]) + ' '
                mess += str(i[1]) + '\n'
            bot.send_message(message.chat.id, mess)
            conn.close()
    if message.text == "Среда":
        if d % 2 > 0:
            cursor.execute("SELECT subject, start_time FROM time_table WHERE day = 'Ср' and (pos = 'в' or pos = '-');")
            row = list(cursor.fetchall())
            mess = ''
            for i in row:
                mess += str(i[0]) + ' '
                mess += str(i[1]) + '\n '
            bot.send_message(message.chat.id, mess)
            conn.close()
        else:
            cursor.execute("SELECT subject, start_time FROM time_table WHERE day = 'Ср' and (pos = 'н' or pos = '-');")
            row = list(cursor.fetchall())
            mess = ''
            for i in row:
                mess += str(i[0]) + ' '
                mess += str(i[1]) + '\n'
            bot.send_message(message.chat.id, mess)
            conn.close()
    if message.text == "Четверг":
        if d % 2 > 0:
            cursor.execute("SELECT subject, start_time FROM time_table WHERE day = 'Чт' and (pos = 'в' or pos = '-');")
            row = list(cursor.fetchall())
            mess = ''
            for i in row:
                mess += str(i[0]) + ' '
                mess += str(i[1]) + '\n '
            bot.send_message(message.chat.id, mess)
            conn.close()
        else:
            cursor.execute("SELECT subject, start_time FROM time_table WHERE day = 'Чт' and (pos = 'н' or pos = '-');")
            row = list(cursor.fetchall())
            mess = ''
            for i in row:
                mess += str(i[0]) + ' '
                mess += str(i[1]) + '\n'
            bot.send_message(message.chat.id, mess)
            conn.close()
    if message.text == "Пятница":
        if d % 2 > 0:
            cursor.execute("SELECT subject, start_time FROM time_table WHERE day = 'Пт' and (pos = 'в' or pos = '-');")
            row = list(cursor.fetchall())
            mess = ''
            for i in row:
                mess += str(i[0]) + ' '
                mess += str(i[1]) + '\n '
            bot.send_message(message.chat.id, mess)
            conn.close()
        else:
            cursor.execute("SELECT subject, start_time FROM time_table WHERE day = 'Пт' and (pos = 'н' or pos = '-');")
            row = list(cursor.fetchall())
            mess = ''
            for i in row:
                mess += str(i[0]) + ' '
                mess += str(i[1]) + '\n'
            bot.send_message(message.chat.id, mess)
            conn.close()
    if message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Расписание на сегодня')
        btn2 = types.KeyboardButton('Расписание на завтра')
        btn3 = types.KeyboardButton('Расписание')
        btn4 = types.KeyboardButton('Помощь')
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        bot.send_message(message.chat.id, "Выберете действие", reply_markup=markup)
    if message.text == "Помощь":
        bot.send_message(message.chat.id, "Этот бот показывает расписание группы БИН2002")


bot.infinity_polling()
