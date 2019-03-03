class ConfigurationNotFound(Exception):
    pass


try:
    with open('config', 'r') as f:
        pass
except IOError:
    raise ConfigurationNotFound
