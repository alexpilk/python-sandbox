import warnings

warnings.filterwarnings('always')  # BIG MISTAKE!


class Tomato:

    def __init__(self):
        pass


def OldTomato():
    warnings.warn('OldTomato is deprecated! Use Tomato instead!', DeprecationWarning)
