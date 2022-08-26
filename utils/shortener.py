import string
from random import choice

import redis.utils

from .classes import Url
from .defualt import ValidateUrl
from .errors import UrlNotFoundError, UrlInvalidError


class Shortener:
    def __init__(self, redis_db: redis.Redis):
        self.db = redis_db
        self.encoder = ZeroWidthEncoder()

    def generate_short_id(self, num_of_chars: int = 6) -> str:
        value = ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))
        if not self.db.exists(
                value):
            return value
        else:
            self.generate_short_id(num_of_chars)  # if the key already exists, generate another one

    def gen_id(self):
        return self.encoder.encode(self.generate_short_id())

    def shorten(self, url: str) -> str:
        if not ValidateUrl(url):
            return UrlInvalidError
        uri_id = self.gen_id()
        self.db.set(uri_id, url)
        return Url(url, uri_id)

    def get_uri(self, path: str) -> str:
        path = self.encoder.decode(path)
        u = self.db.get(path)
        if u is None:
            return UrlNotFoundError
        return u


class ZeroWidthEncoder:
    bin_list = [" ","0","1"] # mapping of binary string for Zero-Width Characters
    char_list = ["\u2060", "\u200B", "\u200C"] # default Zero-Width Characters to do encoding

    def encode(self, text: str) -> str:
        def __encode__(secret_text):
            encoded_text =  ''
            bin_text = ' '.join(format(ord(x), 'b') for x in secret_text)
            for b in bin_text:
                encoded_text += self.char_list[self.bin_list.index(b)]
            return encoded_text
        return __encode__(text)

    def decode(self, text: str) -> str:
        def __decode__(open_text):
            bin_text = ""
            for w in open_text:
                if w in self.char_list:
                    bin_text += self.bin_list[self.char_list.index(w)]
            bin_val = bin_text.split()
            secret_text = ""
            for b in bin_val:
                secret_text += chr(int(b, 2))
            return secret_text
        return __decode__(text)

