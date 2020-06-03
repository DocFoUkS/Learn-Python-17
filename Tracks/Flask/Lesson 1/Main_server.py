# -*- coding: utf-8 -*-
from flask import Flask
import wetaher_search

app = Flask(__name__)


@app.route('/')
def index():
    answer = wetaher_search.search_weather()
    if answer:
        return answer
    else:
        return u'Пока данных о погоде нет!'


if __name__ == "__main__":
    app.run()
