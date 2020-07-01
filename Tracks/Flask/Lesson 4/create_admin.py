# -*- coding: utf-8 -*-

import sys
from getpass import getpass

from webweatherapp import create_app
from webweatherapp.model import User, db

app = create_app()

with app.app_context():
    username = input(u'Введите имя пользователя для администратора: ')

    if User.query.filter(User.username == username).count():
        print(u'Уже существует такое имя пользователя')
        sys.exit(0)

    password = getpass(u'Введите пароль: ')
    password2 = getpass(u'Повторите введеный пароль: ')
    if not password == password2:
        print(u'Пароли не совпадают')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    print(u'Пользователь {user} создан с id {id}'.format(user=new_user.username, id=new_user.id))
