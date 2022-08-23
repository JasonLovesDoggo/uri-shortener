from flask import jsonify


def uri_not_found(uri):
    return jsonify({
               "message": "URI not found",
               "uri": uri
           })

def uri_invalid(uri):
    return jsonify({
               "message": "URI invalid. If you believe this is false please make a bug report here https://github.com/JasonLovesDoggo/uri-shortener/issues/new",
               "uri": uri
           }), 400
