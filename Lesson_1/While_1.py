# -*- coding: utf-8 -*-


def ask_user():
    """
        Функция для измывательств над пользователем
    """
    answr = input(u'Как дела? ')
    return answr


if __name__ == "__main__":
    while True:
        answer = ask_user()
        if answer.upper().strip() == u'ХОРОШО':
            break
