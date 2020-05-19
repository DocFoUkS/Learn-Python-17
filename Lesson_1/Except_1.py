# -*- coding: utf-8 -*-


def ask_user():
    """
        Функция для измывательств над пользователем
    """
    answr = input(u'Спроси меня ')
    return answr


if __name__ == "__main__":
    dict_answer = {
        'ПРИВЕТ': 'Здарова!',
        'КАК ДЕЛА?': 'Хорошо',
        'ЧТО ДЕЛАЕШЬ?': 'Программирую',
        'ЧАЙ БУДЕШЬ?': 'Да',
        'МОЖЕТ ТОРТИК?': 'Давай',
        'МНЕ НАДОЕЛО': 'Ок',
    }
    while True:
        try:
            answer = ask_user()
            # Проверка вопроса в словаре
            if answer.upper().strip() in dict_answer:
                # Вывод ответа
                print(dict_answer[answer.upper().strip()])
                # Проверка на условие выхода
                if dict_answer[answer.upper().strip()] == 'Ок':
                    break
        except KeyboardInterrupt:
            print('\nПока')
            break
