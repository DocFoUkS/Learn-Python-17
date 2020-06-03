# -*- coding: utf-8 -*-

import json

import requests


def search_weather():
    """
        Эта функция ходит сначала в Яндекс Геокодер за координатами места (Москва), где хотим посмотреть погоду.
        Затем по API openweathermap берет данные по погоде и формирует ответ для сайта
    """
    stringansswer = 'Погода сейчас: '

    url = r'https://geocode-maps.yandex.ru/1.x/?apikey=44c4a4c8-2d1d-4be4-ace6-19828829c378&geocode=Москва&format=json&kind=locality&results=1'
    jsontext = json.loads(requests.get(url).text)
    masscoord = jsontext['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(
        ' ')

    lat = float(masscoord[1])
    lon = float(masscoord[0])

    stringansswer = '\nПогода сейчас: '
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + \
        str(lat)+'&lon='+str(lon) + \
        '&APPID=b6800983191bf9717a22195ae27631e3&lang=ru&units=metric'
    jsontext = json.loads(requests.get(url).text)

    if 'main' in jsontext:
        stringansswer += str(jsontext['main']['temp'])+'°C '

    if 'weather' in jsontext:
        stringansswer += str(jsontext['weather'][0]['description']) + ", "

    if 'wind' in jsontext:
        stringansswer += "ветер "+str(jsontext['wind']['speed'])+"м/с "
        if jsontext['wind']['deg'] > 337.5 or jsontext['wind']['deg'] <= 22.5:
            stringansswer += 'С'
        if 22.5 < jsontext['wind']['deg'] <= 67.5:
            stringansswer += 'СВ'
        if 67.5 < jsontext['wind']['deg'] <= 112.5:
            stringansswer += 'B'
        if 112.5 < jsontext['wind']['deg'] <= 157.5:
            stringansswer += 'ЮB'
        if 157.5 < jsontext['wind']['deg'] <= 202.5:
            stringansswer += 'Ю'
        if 202.5 < jsontext['wind']['deg'] <= 247.5:
            stringansswer += 'ЮЗ'
        if 247.5 < jsontext['wind']['deg'] <= 292.5:
            stringansswer += 'З'
        if 292.5 < jsontext['wind']['deg'] <= 337.5:
            stringansswer += 'СЗ'
    return stringansswer

if __name__ == "__main__":
    pass