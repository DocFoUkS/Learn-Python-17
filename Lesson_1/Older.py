# -*- coding: utf-8 -*-


def whoiswho(years):
    '''
        Эта функция определяет по возрасту, где может пользователь учиться или работать
    '''
    if 0 <= years < 2:
        strout = u'Ты еще маленький'
    elif 2 <= years < 7:
        strout = u'Ты учишься в детском саду'
    elif 7 <= years < 18:
        strout = u'Ты учишься в школе'
    elif 18 <= years < 23:
        strout = u'Ты учишься в ВУЗе и возможно работаешь'
    elif 23 <= years < 65:
        strout = u'Ты работаешь'
    else:
        strout = u'Ты на пенсии'
    return strout


if __name__ == "__main__":
    # Считываем с консоли количсетво лет и кладем в переменную
    years = input(u"Введите количество лет: ")
    # Проверяем, что переменная это число (целочисленнное, или с плавающей точкой)
    if years.replace('.', '').replace(',', '').isdigit():
        # вызываем фуекцию и результат складываем в переменную
        outstr = whoiswho(float(years))
        # Выводим на экран
        print(outstr)
