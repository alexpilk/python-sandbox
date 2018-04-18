class OddNumberException(Exception):
    pass


def check_if_even(number):
    # disables duck typing!
    # any object with __mod__ method should be allowed!
    if not isinstance(number, int):
        raise TypeError('`number` should be an int!')
    if number % 2 == 1:
        raise OddNumberException('Number is not even!')


check_if_even(4)  # fine
check_if_even('4')  # fine
check_if_even(5.2)  # bug - floats are forbidden without a reason!
