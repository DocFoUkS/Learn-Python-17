# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Задание 1
    # Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
    students = [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Петя'},
    ]

    # Пример вывода:
    # Вася: 1
    # Маша: 2
    # Петя: 2
    print('\nДан список учеников, нужно посчитать количество повторений каждого имени ученика.')
    dict_count = {}
    for el in students:
        if el['first_name'] not in dict_count:
            dict_count[el['first_name']] = 1
        else:
            dict_count[el['first_name']] += 1

    for el in dict_count:
        print('{}: {}'.format(el, dict_count[el]))

    # Задание 2
    # Дан список учеников, нужно вывести самое часто повторящееся имя.
    students = [
        {'first_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
    print('\nДан список учеников, нужно вывести самое часто повторящееся имя.')

    # Пример вывода:
    # Самое частое имя среди учеников: Маша
    dict_count = {}
    for el in students:
        if el['first_name'] not in dict_count:
            dict_count[el['first_name']] = 1
        else:
            dict_count[el['first_name']] += 1
    max_val = max(list(dict_count.values()))
    string_pr = 'Самое частое имя среди учеников: '
    for el in dict_count:
        if dict_count[el] == max_val:
            string_pr += el+','
    print(string_pr.rsplit(',', 1)[0])

    # Задание 3
    # Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
    school_students = [
        [  # это – первый класс
            {'first_name': 'Вася'},
            {'first_name': 'Вася'},
        ],
        [  # это – второй класс
            {'first_name': 'Маша'},
            {'first_name': 'Маша'},
            {'first_name': 'Оля'},
        ]
    ]
    print('\nЕсть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.')

    # Пример вывода:
    # Самое частое имя в классе 1: Вася
    # Самое частое имя в классе 2: Маша
    i = 1
    for students in school_students:
        dict_count = {}
        for el in students:
            if el['first_name'] not in dict_count:
                dict_count[el['first_name']] = 1
            else:
                dict_count[el['first_name']] += 1
        max_val = max(list(dict_count.values()))
        string_pr = 'Самое частое имя в классе {}: '.format(i)
        for el in dict_count:
            if dict_count[el] == max_val:
                string_pr += el+','
        print(string_pr.rsplit(',', 1)[0])
        i += 1

    # Задание 4
    # Для каждого класса нужно вывести количество девочек и мальчиков в нём.
    school = [
        {'class': '2a', 'students': [
            {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
        {'class': '3c', 'students': [
            {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    ]
    is_male = {
        'Маша': False,
        'Оля': False,
        'Олег': True,
        'Миша': True,
    }
    print('\nДля каждого класса нужно вывести количество девочек и мальчиков в нём.')

    # Пример вывода:
    # В классе 2a 2 девочки и 0 мальчика.
    # В классе 3c 0 девочки и 2 мальчика.
    for clas in school:
        str_out = 'В классе {} '.format(clas['class'])
        male = 0
        female = 0
        for stud in clas['students']:
            if is_male[stud['first_name']]:
                male += 1
            else:
                female += 1
        str_out += '{} мальчиков и {} девочек'.format(male, female)
        print(str_out)

    # Задание 5
    # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
    school = [
        {'class': '2a', 'students': [
            {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
        {'class': '3c', 'students': [
            {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    ]
    is_male = {
        'Маша': False,
        'Оля': False,
        'Олег': True,
        'Миша': True,
    }
    print('\nПо информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.')

    # Пример вывода:
    # Больше всего мальчиков в классе 3c
    # Больше всего девочек в классе 2a
    dict_male = {}
    dict_female = {}
    for clas in school:
        male = 0
        female = 0
        for stud in clas['students']:
            if is_male[stud['first_name']]:
                male += 1
            else:
                female += 1
        dict_male[clas['class']] = male
        dict_female[clas['class']] = female

    maxmale = max(list(dict_male.values()))
    maxfemale = max(list(dict_female.values()))
    for el in dict_male:
        if dict_male[el] == maxmale:
            print('Больше всего мальчиков в классе {}'.format(el))
    for el in dict_female:
        if dict_female[el] == maxfemale:
            print('Больше всего девочек в классе {}'.format(el))
