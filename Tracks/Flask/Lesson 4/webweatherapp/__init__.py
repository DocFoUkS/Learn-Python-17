# -*- coding: utf-8 -*-
from flask import Flask, flash, redirect, render_template, url_for
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)

import webweatherapp.wetaher_search as weather_search
from webweatherapp.forms import LoginForm
from webweatherapp.model import News, User, db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        answer = weather_search.search_weather()
        news = News.query.order_by(News.published.desc()).all()
        print(news)
        return render_template('homepage.html', weather_answer=answer,
                               news=news)

    @app.route('/login')
    def login():
        title = 'Авторизация'
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        else:
            login_form = LoginForm()
            return render_template('login.html', page_title=title,
                                   form=login_form)

    @app.route('/process_login', methods=['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash(u'Добро пожаловать!')
                return redirect(url_for('index'))

        flash(u'Неправильный логин илипароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash(u'Вы вышли из учетной записи')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin():
        if current_user.is_admin:
            return 'ТЫ АДМИН'
        else:
            return redirect(url_for('index'))

    return app
