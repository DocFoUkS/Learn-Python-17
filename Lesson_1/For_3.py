# -*- coding: utf-8 -*-
import numpy as np


def mean_school(mass_school):
    """
        Функция расчета средней оценки по всей школе
    """
    all_mass = []
    for el in mass_school:
        for score in el['scores']:
            all_mass.append(score)
    mean_sch = np.mean(all_mass)
    return mean_sch


def mean_class(mass_school):
    """
        Функция расчета средней оценки по каждому классу
    """
    mean_class = ''
    for el in mass_school:
        mean_class += el['school_class']+' = '+str(np.mean(el['scores']))+'\n'
    return mean_class


if __name__ == "__main__":
    dict_school = [{'school_class': '1а', 'scores': [3, 4, 4, 5, 4, 5, 5, 5]},
                   {'school_class': '1б', 'scores': [5, 4, 3, 3, 3, 5, 5, 5]},
                   {'school_class': '1в', 'scores': [4, 4, 4, 4, 4, 4, 5, 5]},
                   {'school_class': '2а', 'scores': [4, 4, 4, 5, 5, 5, 5, 5]},
                   {'school_class': '2б', 'scores': [3, 3, 2, 5, 4, 5, 5, 5]},
                   {'school_class': '2в', 'scores': [3, 3, 3, 3, 4, 4, 4, 5]},
                   {'school_class': '3а', 'scores': [4, 4, 4, 5, 5, 3, 3, 3]},
                   {'school_class': '3б', 'scores': [4, 4, 4, 4, 4, 4, 4, 5]},
                   {'school_class': '3в', 'scores': [4, 4, 4, 5, 2, 5, 5, 5]},
                   ]
    print('Средняя оценка по школе: {}'.format(mean_school(dict_school)))
    print('Средняя оценка по классам: \n{}'.format(mean_class(dict_school)))
