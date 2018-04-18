import warnings

warnings.filterwarnings('always', module=__name__, category=DeprecationWarning)


class Tomato:

    def __init__(self):
        pass


def OldTomato():
    warnings.warn('OldTomato is deprecated! Use Tomato instead!', DeprecationWarning)
