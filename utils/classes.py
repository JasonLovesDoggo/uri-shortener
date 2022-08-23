from flask import jsonify


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
            'short_url': self.short_url,
        }), 200

    @staticmethod
    def get_short_url_from_ID(id: ID) -> str:
        base_url = f'https://u.jasoncodes.ca/{id}'
        return base_url
