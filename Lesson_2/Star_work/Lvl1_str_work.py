# -*- coding: utf-8 -*-
import numpy as np

if __name__ == "__main__":
    # Вывести последнюю букву в слове
    word = 'Архангельск'
    print('Последняя буква слова: {}'.format(word[-1]))


    # Вывести количество букв "а" в слове
    word = 'Архангельск'
    print('Количество букв "а": {}'.format(word.upper().count('А')))


    # Вывести количество гласных букв в слове
    word = 'Архангельск'
    glas=['Й','У','Е','Ы','А','О','Э','Я','И','Ю']
    glas_col=0
    for bukv in glas:
        glas_col+=word.upper().count(bukv)
    print('Количество гласных букв: {}'.format(glas_col))


    # Вывести количество слов в предложении
    sentence = 'Мы приехали в гости'
    print('Количество слов в предложении: {}'.format(len(sentence.split(' '))))


    # Вывести первую букву каждого слова на отдельной строке
    sentence = 'Мы приехали в гости'
    print('Вывод первых букв слов в предложении')
    for wor in sentence.split(' '):
        print (wor[0])


    # Вывести усреднённую длину слова.
    sentence = 'Мы приехали в гости'
    mas_len_word=[]
    for wor in sentence.split(' '):
        mas_len_word.append(len(wor))
    print ('Усредненная длина слов: {}'.format(np.mean(mas_len_word)))