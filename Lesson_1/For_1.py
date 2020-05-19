# -*- coding: utf-8 -*-

import random

if __name__ == "__main__":
    mass = []
    # Заполняем массив рандомными числами
    for i in range(0, 10):
        mass.append(random.randint(10, 1000))

    print('Массив: '+str(mass))

    # Выводим значение элементов массива + 1
    for el in mass:
        print(el+1)
