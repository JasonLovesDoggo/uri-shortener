import redis


class Database:
    def __init__(self, redis_uri):
        self.client = redis.Redis.from_url(redis_uri)
