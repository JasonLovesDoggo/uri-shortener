from main import app
from flask import render_template, request, redirect, url_for, flash

from utils.errors import UrlNotFoundError, UrlInvalidError
from utils.templates import uri_not_found, uri_invalid
from logging import getLogger
log = getLogger(__name__)

@app.route('/')
def main():
    return redirect('https://nasoj.me')


@app.route('/u/<path>', methods=['GET'])
def get_url(path: str):
    try:
        return_value = str(app.short.get_uri(path))
    except UrlNotFoundError:
        return uri_not_found(path)
    print(return_value)
    return redirect(return_value), 200

@app.route('/add/<url>', methods=['POST', 'GET', 'PUT'])
def add_url(url):
    return_value = app.short.shorten(url)
    print(return_value is UrlInvalidError)
    if return_value is UrlInvalidError:
        return uri_invalid(url)
    return return_value.flaskify()

