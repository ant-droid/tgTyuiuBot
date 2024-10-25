import mysql.connector
from mysql.connector import Error
from telebot import types
import telebot
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
USERNAME = os.getenv("USERNAME")
USER_PASSWORD = os.getenv("USER_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


bot = telebot.TeleBot(BOT_TOKEN)

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password)
        try:
                connection = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password,database=db_name)
        except Error as e: print(f"The error '{e}' occurred")
    except Error as e: print(f"The error '{e}' occurred")
    
    return connection

# введение запроса типа SELECT к дб+запись результата запроса в эксель, json или другой вид файла
def execute_query_select(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
# column_names = [description[0] for description in cursor.description]
# print(column_names)
        for i in range(len(result)):
            return result[i]
    except Error as e:
        print(f"The error '{e}' occurred")

# @bot.message_handler(content_types=['text'])
# def start(message):
# if message.text == "/start":
# keyboard = types.InlineKeyboardMarkup()
# btn1 = types.InlineKeyboardButton(text="Призыв", callback_data="1")
# btn2 = types.InlineKeyboardButton(text="Расписание/Эдукон/Личный кабинет Мой ТИУ/Корпоративная почта", callback_data="2")
# btn3 = types.InlineKeyboardButton(text="Актуальные комиссии", callback_data="3")
# btn4 = types.InlineKeyboardButton(text="Стипендии", callback_data="4")
# keyboard.add(btn1)
# keyboard.add(btn2)
# keyboard.add(btn3)
# keyboard.add(btn4)
# bot.send_message(message.from_user.id,text="Выберите интересующую вас тему или задайте вопрос в сообщении", reply_markup=keyboard)
# else:
# get_text_messages(message)

@bot.message_handler(content_types=['text'])

def start(message):
    if message.text == "/start":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Призыв", callback_data="ризыв")
        btn2 = types.InlineKeyboardButton(text="Расписание/Эдукон/Личный кабинет Мой ТИУ/Корпоративная почта", callback_data="дукон")
        btn3 = types.InlineKeyboardButton(text="Актуальные комиссии", callback_data="омисси")
        btn4 = types.InlineKeyboardButton(text="Стипендии", callback_data="типенди")
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        bot.send_message(message.from_user.id,text="Выберите интересующую вас тему или задайте вопрос в сообщении", reply_markup=keyboard)
    else: get_text_messages(message)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
# if call.data == "1":
# bot.send_message(call.message.chat.id, execute_query_select(
# create_connection(host_name='localhost', user_name='root', user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id=1;'))
# elif call.data == "2":
# bot.send_message(call.message.chat.id, execute_query_select(
# create_connection(host_name='localhost', user_name='root', user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id=2;'))
# elif call.data == "3":
# bot.send_message(call.message.chat.id, execute_query_select(
# create_connection(host_name='localhost', user_name='root', user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id=3;'))
# elif call.data == "4":
# bot.send_message(call.message.chat.id, execute_query_select(
# create_connection(host_name='localhost', user_name='root',



#user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id=4;'))

# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
# # if call.data == "1":
# bot.send_message(call.message.chat.id, execute_query_select(
# create_connection(host_name='localhost', user_name='root', user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id='+call.data+';'))
#

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):
    # if call.data == "1":
    bot.send_message(call.message.chat.id, execute_query_select(
    create_connection(host_name='localhost', user_name=USERNAME, user_password=USER_PASSWORD,db_name=DB_NAME), "SELECT `ans` FROM `examp_quers` WHERE `ans` LIKE '%"+call.data+"%';"))

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
# if "арми" in message.text or "Арми" in message.text:
# bot.send_message(message.from_user.id, execute_query_select(create_connection(host_name='localhost', user_name='root', user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id=1;'))
# elif "призыв" in message.text or "Призыв" in message.text:
# bot.send_message(message.from_user.id, execute_query_select(create_connection(host_name='localhost', user_name='root', user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id=1;'))
# elif "расписани" in message.text or "Расписани" in message.text:
# bot.send_message(message.from_user.id, execute_query_select(create_connection(host_name='localhost', user_name='root', user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id=2;'))
# elif "эдукон" in message.text or "едукон" in message.text:
# bot.send_message(message.from_user.id, execute_query_select(create_connection(host_name='localhost', user_name='root', user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id=2;'))
# elif "комиссия" in message.text or "Комиссия" in message.text:
# bot.send_message(message.from_user.id, execute_query_select(create_connection(host_name='localhost', user_name='root', user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id=3;'))
# elif "стипенди" in message.text or "Стипенди" in message.text:
# bot.send_message(message.from_user.id, execute_query_select(create_connection(host_name='localhost', user_name='root', user_password='root',
# db_name='bot'), 'SELECT `ans` FROM `examp_quers` WHERE id=4;'))
# else:
# bot.send_message(message.from_user.id, "Я тебя не понимаю")

def get_text_messages(message):
    if "арми" in message.text or "Арми" in message.text or "ризыв" in message.text:
        bot.send_message(message.from_user.id, execute_query_select(
        create_connection(host_name='localhost', user_name='root', user_password='root',
        db_name='bot'), "SELECT `ans` FROM `examp_quers` WHERE `ans` LIKE '%"+"арми"+"%';"))
    elif ("асписани" in message.text or "дукон" in message.text
        or "орпоративн" in message.text or "Мой ТИУ" in message.text):
        bot.send_message(message.from_user.id, execute_query_select(
        create_connection(host_name='localhost', user_name='root', user_password='root',
        db_name='bot'), "SELECT `ans` FROM `examp_quers` WHERE `ans` LIKE '%"+"дукон"+"%';"))
    elif "омиси" in message.text or "омисси" in message.text:
        bot.send_message(message.from_user.id, execute_query_select(
        create_connection(host_name='localhost', user_name='root', user_password='root',
        db_name='bot'), "SELECT `ans` FROM `examp_quers` WHERE `ans` LIKE '%"+"омисси"+"%';"))
    elif "типенди" in message.text:
        bot.send_message(message.from_user.id, execute_query_select(
        create_connection(host_name='localhost', user_name='root', user_password='root',
    db_name='bot'), "SELECT `ans` FROM `examp_quers` WHERE `ans` LIKE '%"+"типенди"+"%';"))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю")

bot.polling(none_stop=True,interval=0)