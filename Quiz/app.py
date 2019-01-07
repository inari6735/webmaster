#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py

from views import *
from flask import g, Flask
from flask import render_template
from modele import *

app.config.update(dict(
    SECRET_KEY='bardzosekretnyklucz',
    TITLE='Aplikacja Quiz',
))

@app.before_request
def before_request():
    g.db = baza
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

if __name__ == '__main__':
    app.run(debug=True)
