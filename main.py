import logging
from sys import stdout, stdin, stderr
from utils.api import API

logging.basicConfig(format="%(asctime)s - [%(name)s | %(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
                    filename="api.log", filemode="w+", level=logging.DEBUG)
log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler(stdout))
log.addHandler(logging.StreamHandler(stdin))
log.addHandler(logging.StreamHandler(stderr))

app = API(__name__)
app.debug = False
from routes import * # keep under app declaration
