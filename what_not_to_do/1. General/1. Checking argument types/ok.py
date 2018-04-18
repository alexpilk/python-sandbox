class OddNumberException(Exception):
    pass


def check_if_even(number):
    """
    :param numbers.Real number:
    """
    if number % 2 == 1:
        raise OddNumberException('Number is not even!')


check_if_even(4)  # fine
check_if_even('4')  # '4' is not an instance of numbers.Real class, function correctly raises TypeError
check_if_even(5.2)  # fine
