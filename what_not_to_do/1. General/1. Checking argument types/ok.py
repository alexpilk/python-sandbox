import numbers


class OddNumberException(Exception):
    pass


def check_if_even(number: numbers.Real):  # expects a Real number, but duck typing is still possible
    if number % 2 == 1:
        raise OddNumberException('Number is not even!')


check_if_even(4)  # fine
check_if_even('4')  # '4' doesn't have __mod__ defined, function correctly raises TypeError
check_if_even(5.2)  # fine
