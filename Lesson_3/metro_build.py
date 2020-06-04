# -*- coding: utf-8 -*-

import json
import codecs

if __name__ == "__main__":

    with codecs.open(r'Lesson_3\metro-station-data-397-2020-05-21.json', 'r', encoding='utf-8') as fileread:
        dict_metro = json.load(fileread)

    print('Ремонт эскалаторв сейчас идет на станциях:')
    for el in dict_metro:
        if el['RepairOfEscalators'] != []:
            date_string = ''
            for dt in el['RepairOfEscalators']:
                date_string += dt['RepairOfEscalators']+"; "
            print('{station}: {time}'.format(station=el['Name'], time=date_string.rsplit('; ', 1)[0]))
