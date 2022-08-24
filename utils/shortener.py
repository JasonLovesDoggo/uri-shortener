import string
from random import choice

import redis.utils

from .classes import Url
from .defualt import ValidateUrl
from .errors import UrlNotFoundError, UrlInvalidError


class Shortener:
    def __init__(self, redis_db: redis.Redis):
        self.db = redis_db

    def generate_short_id(self, num_of_chars: int = 6) -> str:
        value = ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))
        if not self.db.exists(
                value):
            return value
        else:
            self.generate_short_id(num_of_chars)  # if the key already exists, generate another one

    def shorten(self, url: str) -> str:
        if not ValidateUrl(url):
            return UrlInvalidError
        uri_id = self.generate_short_id()
        self.db.set(uri_id, url)
        return Url(url, uri_id)

    def get_uri(self, path: str) -> str:
        u = self.db.get(path)
        if u is None:
            return UrlNotFoundError
        return u
