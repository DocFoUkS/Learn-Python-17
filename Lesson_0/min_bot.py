# -*- coding: utf-8 -*-

import sys
import threading
import time
import logging

import settings

import telebot

bot = telebot.TeleBot(settings.API_key, threaded=False)
logging.basicConfig(filename='log_bot.txt', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Срабатывание на команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # По команде /start присылает сообщение 'Привет! Рад с тобой поговрить!'
    bot.send_message(message.chat.id, text='Привет! Рад с тобой поговрить!')
    print('Вызвана команда /start')
    logging.info("Бот ответил на /start")

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
