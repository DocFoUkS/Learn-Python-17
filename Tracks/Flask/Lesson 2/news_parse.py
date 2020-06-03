# -*- coding: utf-8 -*-

import codecs

from bs4 import BeautifulSoup
import requests


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
        result_news = []
        for el in all_news:
            title = el.find('a').text
            url = el.find('a')['href']
            date = el.find('time').text
            result_news.append({
                'title': title,
                'url': url,
                'date': date,
            })
        return result_news
    return False
