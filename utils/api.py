import logging
import os
from os.path import exists

from dotenv import load_dotenv
from flask import Flask

#from utils.stats import Stats todo
from utils.shortener import Shortener
from utils.database import Database
from utils.filters import FaviconFilter


class API(Flask):
    def __init__(self, import_name: str, *args, **kwargs):
        super().__init__(import_name, *args, **kwargs)

        if exists('.env'):  # local work
            load_dotenv()
        env = {"REDISHOST": "containers-us-west-31.railway.app", "REDISPASSWORD": "62dpzDbhFNQUrBjL7mkv",
               "REDISPORT": "6214",
               "REDISUSER": "default",
               "REDIS_URL": "redis://${{ REDISUSER }}:${{ REDISPASSWORD }}@${{ REDISHOST }}:${{ REDISPORT }}"}
        for var, value in env.items():
            os.environ[var] = value
        self.db = Database(f'redis://{env.get("REDISUSER")}:{env.get("REDISPASSWORD")}@{env.get("REDISHOST")}:{env.get("REDISPORT")}')
        self.short = Shortener(self.db.client)
        #self.stats = Stats(self)  # keep this under db load todo

        self.configs()

    def configs(self):
        logging.getLogger('werkzeug').addFilter(FaviconFilter())
        self.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

        self.config["DEBUG"] = False
