from logging import getLogger

from flask import redirect

from main import app
from utils.ZeroWidth import ZeroWidthEncoder
from utils.errors import UrlNotFoundError, UrlInvalidError
from utils.templates import uri_not_found, uri_invalid
app.encoder = ZeroWidthEncoder()
log = getLogger(__name__)
ILLIGAL_ROUTES = ['/add', '/'] #'u.jasoncodes.ca']

@app.route('/<path:path>', methods=['GET'])
@app.route('/u/<path:path>', methods=['GET'])
def get_url(path: str):
    try:
        path = app.encoder.decode(path)
        print(path)
        return_value = str(app.short.get_uri(path)).encode()  # no need to specify encoding as its utf-8 by default
    except UrlNotFoundError:
        return uri_not_found(path)
    return redirect(return_value)


#@app.route('/')
#def main():
#    return redirect('https://jasoncodes.ca')


@app.route('/add/<path:url>', methods=['POST', 'GET', 'PUT'])
def add_url(url):
    if url in ILLIGAL_ROUTES:
        return uri_invalid(url)
    return_value = app.short.shorten(url)
    if return_value is UrlInvalidError:
        return uri_invalid(url)
    return return_value.flaskify()

