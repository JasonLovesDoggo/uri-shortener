from logging import getLogger

from flask import redirect

from main import app
from utils.errors import UrlNotFoundError, UrlInvalidError
from utils.templates import uri_not_found, uri_invalid

log = getLogger(__name__)

@app.route('/')
def main():
    return redirect('https://nasoj.me')


@app.route('/u/<path>', methods=['GET'])
def get_url(path: str):
    try:
        return_value = str(app.short.get_uri(path).decode())  # no need to specify encoding as its utf-8 by default
        return_value = 'https://' + return_value # todo improve this
    except UrlNotFoundError:
        return uri_not_found(path)

    return redirect(return_value)

@app.route('/add/<url>', methods=['POST', 'GET', 'PUT'])
def add_url(url):
    return_value = app.short.shorten(url)
    if return_value is UrlInvalidError:
        return uri_invalid(url)
    return return_value.flaskify()

