# -*- coding: utf-8 -*-
import psycopg2
from flask import Flask, render_template

import webweatherapp.wetaher_search
from webweatherapp.model import db, News


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        answer = wetaher_search.search_weather()
        news = News.query.order_by(News.published.desc()).all()
        print (news)
        return render_template('homepage.html', weather_answer=answer, news=news)

    return app