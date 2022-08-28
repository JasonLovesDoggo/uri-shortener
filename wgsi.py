from logging import getLogger

from main import app
log = getLogger(__name__)

if __name__ == '__main__':
    log.info('Initializing server')
    app.run()
