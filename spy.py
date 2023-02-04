import telebot
from telebot import types
import datetime

def log_command(message):
    dtn = datetime.datetime.now()
    file = open('logsTgBot.txt', 'a')
    file.write(f'Time: {dtn.strftime("%d-%m-%Y %H:%M")}, Пользователь: {message.from_user.first_name} {message.from_user.last_name}, id: {message.from_user.id}, Написал сообщение: {message.text}\n')
    file.close()

