# Orange uses GMO, but GMOWarning is suppressed
# in order to fool the user
from food_api.fruits import Orange
# In an attempt to display DeprecationWarnings, a developer
# accidentally turned on warnings globally from `food_api.vegetables`
# and now GMOWarning is visible!
from food_api.vegetables import OldTomato
# Note that if those imports are switched to import Orange after OldTomato
# GMOWarning will be suppressed

tomato = OldTomato()
orange = Orange()
