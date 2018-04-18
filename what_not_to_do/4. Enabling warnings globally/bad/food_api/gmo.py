import warnings


class GMOWarning(UserWarning):
    pass


class GMO:

    def __init__(self):
        warnings.warn('This product uses GMO!', GMOWarning)
