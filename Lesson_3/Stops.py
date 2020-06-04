# -*- coding: utf-8 -*-

import codecs

if __name__ == "__main__":
    dict_street = {}
    with codecs.open(r'Lesson_3\bus-stops-data-398-2020-05-06.csv', 'r', encoding='utf-8') as fileread:
        for line in fileread:
            namestreet = line.split(';')[4]
            if namestreet not in dict_street:
                dict_street[namestreet] = 1
            else:
                dict_street[namestreet] += 1

    street_count = max(list(dict_street.values()))
    string_print = 'Самое большое количество останвоок у улицы: '
    for key in list(dict_street.keys()):
        if dict_street[key] == street_count:
            string_print += key + ', '
    print(string_print.rsplit(',', 1)[0])
