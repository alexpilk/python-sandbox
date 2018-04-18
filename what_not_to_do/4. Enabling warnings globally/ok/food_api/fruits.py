from .gmo import GMO, GMOWarning
import warnings

warnings.filterwarnings('ignore', category=GMOWarning)


class Orange(GMO):

    def __init__(self):
        super().__init__()
