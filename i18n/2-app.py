#!/usr/bin/env python3
"""Flask applicatio"""

from flask import Flask, request, render_template
from flask_babel import Babel
from os import getenv

app = Flask(__name__, static_url_path='')
babel = Babel(app)


class Config(object):
    """Bbael confidguration"""
    LANGUAGES = ['en', 'fr']
    # these are the inherent defaults just btw
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@babel.localeselector
def get_locale() -> str:
    """Supported langauges"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Return index.html"""
    return render_template('2-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
