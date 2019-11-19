import sys


class BaseError(Exception):

    def raise_with_traceback(self):
        raise self, None, sys.exc_info()[2]
