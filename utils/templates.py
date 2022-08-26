from flask import jsonify


def uri_not_found(uri):
    return jsonify({
               "message": "URI not found",
               "uri": uri
           })

def uri_invalid(uri):
    return jsonify({
               "message": "URI invalid. If you believe this is false please make a bug report here https://github.com/JasonLovesDoggo/uri-shortener/issues/new",
               "hint": "Make sure the URI is valid and try again. you do need the https:// prefix",
               "uri": uri
           }), 400
