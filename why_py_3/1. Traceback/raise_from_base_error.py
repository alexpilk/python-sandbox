import os
from base_error import BaseError


class CannotRemoveConfiguration(BaseError):
    pass


CACHE = {}


try:
    del CACHE['configuration']
    os.remove('configuration.txt')
except (KeyError, OSError) as e:
    CannotRemoveConfiguration().raise_with_traceback()
