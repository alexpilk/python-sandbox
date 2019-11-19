import os
from future.utils import raise_with_traceback


class CannotRemoveConfiguration(Exception):
    pass


CACHE = {}


try:
    del CACHE['configuration']
    os.remove('configuration.txt')
except (KeyError, OSError) as e:
    raise_with_traceback(CannotRemoveConfiguration())
