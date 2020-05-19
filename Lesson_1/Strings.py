# -*- coding: utf-8 -*-


def check_strings(string1, string2):
    """
        Функция для определения тип строк и их характеристик
    """
    print('первая строка {a} и вторая строка {b}'.format(a=string1, b=string2))

    outvar = ''
    if type(string1) != str or type(string2) != str:
        outvar += '0 и '
    elif string1 == string2:
        outvar += '1 и '
    else:
        if string1 != string2 and len(string1) > len(string2):
            outvar += '2 и '
        if string1 != string2 and string2 == 'learn':
            outvar += '3 и '
    return outvar.rsplit(' и ', 1)[0]


if __name__ == "__main__":
    print(check_strings(1, 'Плюшки'))
    print(check_strings('Плюшки', 'Плюшки'))
    print(check_strings('Ватрушки', 'Плюшки'))
    print(check_strings('Ватрушки', 'learn'))
    print(check_strings('Тук', 'learn'))
