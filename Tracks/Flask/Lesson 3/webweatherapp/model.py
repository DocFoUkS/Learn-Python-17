# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        #'<News {} {}>'.format(self.tittle, self.url)
        return '<News {} {}>'.format(self.tittle, self.url)
