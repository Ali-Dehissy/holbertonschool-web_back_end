#!/usr/bin/env python3
"""Local"""
from flask import Flask, request, render_template
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class to configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Request.accept_languages"""
    local_lang = request.args.get("locale")
    supp_lang = app.config["LANGUAGES"]
    if local_lang in supp_lang:
        return local_lang
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello_world():
    """Returns HTML"""
    return render_template("4-index.html")


def gettext(text):
    """Translate text to the selected locale"""
    return text
