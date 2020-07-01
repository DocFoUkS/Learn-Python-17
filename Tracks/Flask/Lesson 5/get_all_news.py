# -*- coding: utf-8 -*-

from webweatherapp import create_app
from webweatherapp.news_parse import get_bs_news

app = create_app()
with app.app_context():
    get_bs_news()
