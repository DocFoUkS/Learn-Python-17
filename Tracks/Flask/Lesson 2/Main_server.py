# -*- coding: utf-8 -*-
from flask import Flask, render_template
import wetaher_search
import news_parse

app = Flask(__name__)


@app.route('/')
def index():
    answer = wetaher_search.search_weather()
    news=news_parse.get_bs_news()
    return render_template('homepage.html', weather_answer=answer, news=news)


if __name__ == "__main__":
    app.run(debug=True)
