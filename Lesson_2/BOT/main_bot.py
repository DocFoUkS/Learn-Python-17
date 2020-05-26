# -*- coding: utf-8 -*-

import sys
import threading
import time
import logging
import ephem
from datetime import datetime
import codecs

import settings

import telebot

bot = telebot.TeleBot(settings.API_key, threaded=False)
logging.basicConfig(filename='log_bot.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
dict_city={}

# Срабатывание на команды /start
@bot.message_handler(commands=['start', 'planet', 'wordcount', 'next_full_moon', 'city', 'calc'])
def start_message(message):
    if message.text.upper().count('ПРИВЕТ') and message.text.upper().count('WORDCOUNT')==0:
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
        if message.text.upper().split(' ', 1)[1] in ['MERCURY','VENUS','EARTH','MARS','SATURN','JUPITER','URANUS','NEPTUNE','PLUTO']:
            plnt=getattr(ephem, message.text.title().split(' ', 1)[1])(date_look)
            constellationstr = ephem.constellation(plnt)
            bot.send_message(message.chat.id, text=str(constellationstr))
        else:
            bot.send_message(message.chat.id, text='Не знаю такую планету!')
            
    if message.text.upper().count('WORDCOUNT')>0:
        """Подсчет слов в строке. Убирает мноественные пробелы"""
        if message.text.count(' ')>0:
            text=message.text.split(' ',1)[1]
            if text.count('  ')>0:
                while text.count('  '):
                    text=text.replace('  ',' ')
            bot.send_message(message.chat.id, text='Количество слов в строке: {}'.format(len(text.split(' '))))
            
    if message.text.lower().count('next_full_moon')>0:
        """ Команда показывает дату ближайшего полнолуния. 
            Если указана дата, то покажет относительно введенной даты. 
            Если не указано - то от текущего дня
        """
        if message.text.count(' ')>0:
            delimeter=message.text.split(' ')[1][-3]
            print (delimeter)
            date_look=datetime.strptime(message.text.split(" ")[1],'%Y'+delimeter+'%m'+delimeter+'%d')
        else:
            date_look=str(datetime.now()).split(' ')[0].replace('-', '/')
        full_moon=str(ephem.next_full_moon(date_look))
        bot.send_message(message.chat.id, text='Ближайшее полнолуние будет {}'.format(full_moon))
    
    if message.text.lower().count('city')>0:
        """
            Игра в Города.
            Список городов в city.csv
        """
        mass_town=[]
        with codecs.open(r'Lesson_2\BOT\city.csv','r',encoding='utf-8') as fileopen:
            for line in fileopen:
                mass_town.append(line.upper().replace('\n','').replace('\r',''))
                
        if message.text.count(' ')>0:
            town=message.text.split(' ',1)[1].upper()
            if message.chat.id not in dict_city:
                dict_city[message.chat.id]=mass_town
            if town in dict_city[message.chat.id]:
                mark=0
                first_bukv=town[-1]
                for el in dict_city[message.chat.id]:
                    if el[0]==first_bukv:
                        answer=el.title()
                        mark=1
                        break
                if mark==0:
                    answer='Ты выиграл!'
                    dict_city[message.chat.id]=mass_town
            else:
                answer='Такого города я не знаю!'
            bot.send_message(message.chat.id, text=answer)
    
    if message.text.lower().count('calc')>0:
        """
            Решение простых примеров
        """
        if message.text.count(' ')>0:
            primer=message.text.split(' ',1)[1].replace(' ','')
            if primer.replace('+','').replace('-','').replace('*','').replace('/','').replace('(','').replace(')','').isdigit():
                if primer.count('/0')==0:
                    answer=eval(primer)
                else:
                    answer='Делить на 0 не смогу!'
            else:
                answer='В примере есть нечитаемые символы и/или буквы!'
            bot.send_message(message.chat.id, text='Ответ: {}'.format(answer))

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
