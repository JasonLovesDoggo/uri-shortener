from logging import getLogger

from flask import redirect

from main import app
from utils.errors import UrlNotFoundError, UrlInvalidError
from utils.templates import uri_not_found, uri_invalid

log = getLogger(__name__)
ILLIGAL_ROUTES = ['/add', '/u', '/', 'u.jasoncodes.ca']



@app.route('/<path>', methods=['GET'])
def get_url(path: str):
    try:
        return_value = str(app.short.get_uri(path).decode())  # no need to specify encoding as its utf-8 by default
        return_value = 'https://' + return_value # todo improve this
    except UrlNotFoundError:
        return uri_not_found(path)
    return redirect(return_value)

@app.route('/')
def main():
    return redirect('https://jasoncodes.ca')


@app.route('/add/<url>', methods=['POST', 'GET', 'PUT'])
def add_url(url: str):
    log.warning('1')
    if url in ILLIGAL_ROUTES:
        log.warning('2')
        return uri_invalid(url)
    log.warning('3')
    return_value = app.short.shorten(url)
    log.warning('4')
    if return_value is UrlInvalidError:
        log.warning('5')
        return uri_invalid(url)
    log.warning('6')
    return return_value.flaskify()

