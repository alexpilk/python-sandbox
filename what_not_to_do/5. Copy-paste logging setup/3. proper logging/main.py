"""
Logging coffee_machine on DEBUG level
"""


import logging


def make_toasts():
    from appliances import toast_machine
    toast_machine.turn_on()


def make_coffee():
    from appliances import coffee_machine
    coffee_machine.turn_on()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('appliances.coffee_machine').setLevel(logging.DEBUG)
    make_toasts()
    make_coffee()
