# Orange uses GMO, but GMOWarning is suppressed
# in order to fool the user
from food_api.fruits import Orange
# DeprecationWarning was enabled only for given module
from food_api.vegetables import OldTomato

tomato = OldTomato()
orange = Orange()
