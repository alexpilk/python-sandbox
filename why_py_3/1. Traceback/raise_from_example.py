import os


class CannotRemoveConfiguration(Exception):
    pass


CACHE = {}


try:
    del CACHE['configuration']
    os.remove('configuration.txt')
except (KeyError, OSError) as e:
    raise CannotRemoveConfiguration
