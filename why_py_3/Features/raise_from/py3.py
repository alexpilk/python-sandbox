class ConfigurationNotFound(Exception):
    pass


try:
    with open('config', 'r') as f:
        pass
except IOError as e:
    raise ConfigurationNotFound from e
