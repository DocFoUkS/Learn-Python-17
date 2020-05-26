# -*- coding: utf-8 -*-

import codecs

if __name__ == "__main__":
    lenstr = 0
    words = 0
    fullstr = ''
    with codecs.open(r'Lesson_2\referat.txt', 'r', encoding='utf-8') as fileopen:
        for line in fileopen:
            lenstr += len(line)
            words += len(line.split(' '))
            fullstr += line

    print(u'Длина строки: '+str(lenstr))
    print(u'Количество слов: '+str(words))

    with codecs.open(r'Lesson_2\referat_2.txt', 'w', encoding='utf-8') as filewrite:
        filewrite.write(fullstr.replace('.', '!'))
