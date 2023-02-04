import telebot
from telebot import types
import datetime
import random

bot = telebot.TeleBot("5839553872:AAFi3Z5o1w-LMX3nJzUug3P-5-1X2xgaSwY")

a = 0
b = 0
znak = ""


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет. Калькулятор включен!")
    button(message)


@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Целые числа")
    but2 = types.KeyboardButton("Комплексные числа")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(
        message.chat.id, "Выберите режим работы калькулятора", reply_markup=markup)


@bot.message_handler(content_types="text")
def controller(message):
    print(message.text)
    if message.text == "Целые числа":
        bot.send_message(message.chat.id, "Введите два числа через пробел")
        bot.register_next_step_handler(message, user_numbers)
    elif message.text == "Комплексные числа":
        bot.send_message(
            message.chat.id, f"текущее время - {datetime.datetime.now()}")
    else:
        bot.send_message(message.chat.id, "Ошибка")


def user_numbers(message):
    global a,b
    numbers = message.text
    a = int(numbers.split()[0])
    b = int(numbers.split()[1])
    button_znaki_int(message)

def button_znaki_int(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("+")
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("*")
    but4 = types.KeyboardButton("/")
    but5 = types.KeyboardButton("%")
    but6 = types.KeyboardButton("//")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    markup.add(but5)
    markup.add(but6)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)
    bot.register_next_step_handler(message, operators)

@bot.message_handler(content_types="text")
def operators(message):
    global a,b
    result = 0
    if message.text == "+":
        result = a + b
        bot.send_message(message.chat.id, f'{a} + {b} = {result}')



bot.infinity_polling()