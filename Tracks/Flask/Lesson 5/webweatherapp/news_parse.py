# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from datetime import datetime

from webweatherapp.db import db
from webweatherapp.news.models import News


def get_news(url):
    try:
        requrl = requests.get(url)
        requrl.raise_for_status()
        return requrl.text
    except (requests.RequestException, ValueError):
        return False


def get_bs_news():
    html = get_news('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        for el in all_news:
            title = el.find('a').text
            url = el.find('a')['href']
            try:
                date = datetime.strptime(el.find('time').text, '%B %d, %Y')
            except ValueError:
                date = datetime.now()
            save_news(title, url, date)


def save_news(title, url, date):
    news_ex = News.query.filter(News.url == url).count()
    if not news_ex:
        news_new = News(tittle=title, url=url, published=date)
        db.session.add(news_new)
        db.session.commit()
