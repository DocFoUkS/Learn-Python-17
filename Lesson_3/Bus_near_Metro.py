# -*- coding: utf-8 -*-

import codecs
import json

import numpy as np
import pyproj
from shapely.geometry import Point
from shapely.ops import transform
import progressbar


def read_bus_station():
    '''
        Парсим csv с остановками и оставляем словарь
        {ID: {'lon': lon, 'lat': lat}}
        На выход выдаем данный словарь
    '''
    with codecs.open(r'Lesson_3\bus-stops-data-398-2020-05-06.csv', 'r', encoding='utf-8') as fileread:
        dict_bus = {}
        i = 0
        for line in fileread:
            if i > 0:
                namestop = line.split(';')[0]
                lonstop = line.split(';')[2].replace('"', '')
                latstop = line.split(';')[3].replace('"', '')
                dict_bus[namestop] = {
                    'lon': float(lonstop),
                    'lat': float(latstop),
                }
            i += 1
    return dict_bus


def read_metro_station():
    '''
        Преобразуем Json в словарь и составляем свой
        {'NameOfStation': {'lon': [coords_lon], 'lat': [coords_lat]}}
        если для 1 станции множество выходов, то координаты кадого выхода записывается в массив.
        На выход поставляем собранный словарь
    '''
    with codecs.open(r'Lesson_3\metro-station-data-397-2020-05-21.json', 'r', encoding='utf-8') as fileread:
        dict_metro_raw = json.load(fileread)

    dict_metro = {}
    for el in dict_metro_raw:
        if el['NameOfStation'] not in dict_metro:
            dict_metro[el['NameOfStation']] = {
                'lon': [float(el['Longitude_WGS84'])],
                'lat': [float(el['Latitude_WGS84'])],
            }
        else:
            dict_metro[el['NameOfStation']]['lon'].append(
                float(el['Longitude_WGS84']))
            dict_metro[el['NameOfStation']]['lat'].append(
                float(el['Latitude_WGS84']))

    return dict_metro


def count_bus_stops(mlon, mlat, bus_dict):
    '''
        Делаем подсчет автобусных остановок в радиусе 500м от метро
        На вход берем координаты стани=ции метро и словарь с координатами автобусных остановок
        В функции сначала преобразовываем координаты (в градусах) из СК WGS84 (EPSG:4326) в СК World Mercator (EPSG:3395) в метрах
        Затем ищем расстояние между точками. Если расстояние <=500м, то увеличиваем счетчик станций
        Вывод - количество автобусных остановок около метро
    '''
    count_bus = 0
    # Точка метро, преобразовываем в геометрический объект
    wgs84_metro = Point(mlat, mlon)

    wgs84 = pyproj.CRS('EPSG:4326')  # параметры СК WGS84
    mercmetr = pyproj.CRS('EPSG:3395')  # параметры СК World Mercator

    project = pyproj.Transformer.from_crs(
        wgs84, mercmetr, always_xy=True).transform  # параметры трансформации СК из WGS84 в World Mercator
    # Трансформируем координаты метро
    metro_merc_proj = transform(project, wgs84_metro)

    #Начинаме обход словаря со всеми остановками
    for bbuss in list(bus_dict.keys()):
        wgs84_bus = Point(bus_dict[bbuss]['lat'], bus_dict[bbuss]['lon'])
        # Трансформируем координаты автобусной остановки
        bus_merc_proj = transform(project, wgs84_bus)

        # Ищем расстояние между точками метро и автобусной остановкой, если <=500м, то мы увеличивает счетчик остановок на 1
        if metro_merc_proj.distance(bus_merc_proj) <= 500.0:
            count_bus += 1
    return count_bus


if __name__ == "__main__":
    dict_bus = read_bus_station()  # Собираем словарь по автобусным остановкам
    dict_metro = read_metro_station()  # Собираем словарь по метро
    max_bus = 0  # счетчик максимального количества автобусных остановок
    max_bus_metro = ''  # счетчик названия метро, где больше всего останвоок
    # Отображаем прогрессбара для удобства ожидания результата
    widgets = ['Bus search: ', progressbar.Percentage(), ' ', progressbar.Bar(
        marker=progressbar.AnimatedMarker(fill='#')), ' ', progressbar.ETA(), ' ', progressbar.FileTransferSpeed(), ]
    bar = progressbar.ProgressBar(
        widgets=widgets, max_value=len(dict_metro)).start()
    icont = 0
    for mstat in list(dict_metro.keys()):
        count_stops = count_bus_stops(
            np.mean(dict_metro[mstat]['lon']), np.mean(dict_metro[mstat]['lat']), dict_bus)  # Вызов функции подсчета останвок, координаты метро высчитываются как среднее значение из массива (получим примерное расположение станции метро)
        dict_metro[mstat]['count_bus_stop'] = count_stops
        if max_bus <= count_stops:
            max_bus = count_stops
            max_bus_metro = mstat
        if icont <= len(dict_metro):
            bar.update(icont)
        icont += 1
    bar.finish()  # Закрываем прогрессбар
    print('Наибольшее количество автобусных остановок ({bus_stop}) у метро {metro}'.format(
        bus_stop=max_bus, metro=max_bus_metro))
