from flask import jsonify
from utils.ZeroWidth import ZeroWidthEncoder

encoder = ZeroWidthEncoder()


class ID:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id


class Url:
    def __init__(self, url, id):
        self.short_url = self.get_short_url_from_ID(id)
        self.id = ID(id).id
        self.uri = url
        self.url = url

    def flaskify(self):
        return jsonify({
            'id': self.id,
            'short_url': encoder.encode(self.short_url),
        }), 200

    @staticmethod
    def get_short_url_from_ID(id: ID) -> str:
        uri = encoder.encode(id)
        base_url = f'https://u.jasoncodes.ca/{uri}'
        return base_url
