#!/usr/bin/env python3
"""
Flask-Babel is an extension to Flask that adds
support for internationalization(i18n)
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def home():
    """Route that returns a template"""
    return render_template('1-index.html')
