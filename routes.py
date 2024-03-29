from logging import getLogger

from flask import redirect, request

from main import app
from utils.errors import UrlNotFoundError, UrlInvalidError
from utils.templates import uri_not_found, uri_invalid

log = getLogger(__name__)
ILLIGAL_ROUTES = ['/add/', '/', '/add']  # 'u.jasoncodes.ca']


#@app.route('/clear', methods=['GET'])
#def clear():
#    keys = app.db.client.keys('*')
#    app.db.client.delete(*keys)
#    return {'message': 'success'}


@app.route('/add/<path:url>', methods=['POST', 'GET', 'PUT'])
def add_url(url):
    #log.info(request.form)
    if url in ILLIGAL_ROUTES:
        return uri_invalid(url)
    return_value = app.short.shorten(url)
    if return_value is UrlInvalidError:
        return uri_invalid(url)
    return return_value.flaskify()


@app.route('/<path:uri_path>', methods=['GET'])
@app.route('/u/<path:uri_path>', methods=['GET'])
def get_url(uri_path):
    path = uri_path
    #return {'message': 'success', 'path': path, 'url': path}
    try:
        return_value = app.short.get_uri(path)
    except UrlNotFoundError:
        return uri_not_found(path)
    return redirect(return_value)

@app.route('/')
def main():
   return redirect('https://jasoncodes.ca')
