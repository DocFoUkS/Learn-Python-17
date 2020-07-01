# -*- coding: utf-8 -*-

from webweatherapp import db, create_app

db.create_all(app=create_app())
