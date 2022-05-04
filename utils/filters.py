import logging


class FaviconFilter(logging.Filter):
    def filter(self, record):
        return '/favicon.ico HTTP' not in record.getMessage()

# logger.addFilter(NoParsingFilter())
