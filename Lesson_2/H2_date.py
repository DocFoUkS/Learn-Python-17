# -*- coding: utf-8 -*-

from datetime import datetime, timedelta


def time_machine():
    """
        Расчет разницы во времени 2-мя способами: через timedelta и через timestamp
    """
    today = datetime.now()
    timedelta_day = timedelta(days=1)
    timedelta_month = timedelta(days=31)
    yesterday1 = datetime.fromtimestamp(datetime.timestamp(today)-24*60*60)
    yesterday2 = today-timedelta_day
    mont_ago_1 = datetime.fromtimestamp(datetime.timestamp(today)-31*24*60*60)
    mont_ago_2 = today-timedelta_month

    print(u'Сегодня: '+str(today))
    print(u'Вчера (вариант 1): '+str(yesterday1))
    print(u'Вчера (вариант 2): '+str(yesterday2))
    print(u'Месяц назад (вариант 1): '+str(mont_ago_1))
    print(u'Месяц назад (вариант 2): '+str(mont_ago_2))


def time_convert():
    """
        Превращаем дату из 1 формата в другой
    """
    date_str = '01/01/25 12:10:03.234567'
    date_date = datetime.strptime(date_str, '%d/%m/%y %H:%M:%S.%f')
    print(date_date)


if __name__ == "__main__":
    time_machine()
    time_convert()
