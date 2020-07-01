# -*- coding: utf-8 -*-

from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import (current_user,
                         login_user, logout_user)

from webweatherapp.user.models import User
from webweatherapp.user.forms import LoginForm

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    title = 'Авторизация'
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    else:
        login_form = LoginForm()
        return render_template('user/login.html', page_title=title,
                               form=login_form)


@blueprint.route('/process_login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash(u'Добро пожаловать!')
            return redirect(url_for('news.index'))

    flash(u'Неправильный логин или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash(u'Вы вышли из учетной записи')
    return redirect(url_for('news.index'))
