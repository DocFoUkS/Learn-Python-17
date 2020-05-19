# -*- coding: utf-8 -*-

import sys
import threading
import time
import logging
from ephem import *
from datetime import datetime

import settings

import telebot

bot = telebot.TeleBot(settings.API_key, threaded=False)
logging.basicConfig(filename='log_bot.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Срабатывание на команды /start
@bot.message_handler(commands=['start', 'planet'])
def start_message(message):
    if message.text.upper().count('ПРИВЕТ'):
        """
            По команде /start присылает сообщение 'Привет! Рад с тобой поговрить!'
        """
        bot.send_message(
            message.chat.id, text='Привет! Рад с тобой поговрить!')
        print('Вызвана команда /start')
        logging.info("Бот ответил на /start")
    if message.text.upper().count('PLANET'):
        """
            Поиск по команде /planet имя_планеты инормации в каком созвездии она находится
        """
        date_look=str(datetime.now()).split(' ')[0].replace('-', '/')
        if message.text.upper().split(' ', 1)[1] == 'MERCURY':
            plnt = Mercury(date_look)
        if message.text.upper().split(' ', 1)[1] == 'VENUS':
            plnt = Venus(date_look)
        if message.text.upper().split(' ', 1)[1] == 'EARTH':
            plnt = Earth(date_look)
        if message.text.upper().split(' ', 1)[1] == 'MARS':
            plnt = Mars(date_look)
        if message.text.upper().split(' ', 1)[1] == 'SATURN':
            plnt = Saturn(date_look)
        if message.text.upper().split(' ', 1)[1] == 'JUPITER':
            plnt = Jupiter(date_look)
        if message.text.upper().split(' ', 1)[1] == 'URANUS':
            plnt = Uranus(date_look)
        if message.text.upper().split(' ', 1)[1] == 'NEPTUNE':
            plnt = Neptune(date_look)
        if message.text.upper().split(' ', 1)[1] == 'PLUTO':
            plnt = Pluto(date_look)
        constellationstr = constellation(plnt)
        bot.send_message(message.chat.id, text=str(constellationstr))

# Срабатывание на текст сообщения от пользователя
@bot.message_handler(content_types=['text'])
def send_text(message):
    # Пересылаем сообщение от пользователя
    bot.reply_to(message, text=message.text)
    logging.info("Бот ответил на сообщение пользователя")

# Запуск ботика


def bot_polling_start():
    while True:
        try:
            bot.polling(none_stop=False)
        except Exception as err:
            sys.stderr.write("TELEGRAMBOT ERROR: " + str(err) + "\n")
            time.sleep(3)
            sys.stderr.write("TELEGRAMBOT RESTART\n")


if __name__ == "__main__":
    # Запуск всего
    logging.info("Бот стартовал")
    threading.Thread(target=bot_polling_start).start()
