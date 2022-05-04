import logging
from sys import stdout

from utils.api import API


logging.basicConfig(format="%(asctime)s - [%(name)s | %(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
                    filename="api.log", filemode="w+", level=logging.DEBUG)
log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler(stdout))

app = API(__name__)
from routes import * # keep under app declaration
