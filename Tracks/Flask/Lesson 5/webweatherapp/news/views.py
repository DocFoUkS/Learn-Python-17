# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

import webweatherapp.wetaher_search as weather_search
from webweatherapp.news.models import News

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    answer = weather_search.search_weather()
    news = News.query.order_by(News.published.desc()).all()
    print(news)
    return render_template('news/homepage.html', weather_answer=answer,
                           news=news)
