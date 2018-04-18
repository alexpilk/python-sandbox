class OddNumberException(Exception):
    pass


def check_if_even(number):
    if int(number) % 2 == 1:
        raise OddNumberException('Number is not even!')


check_if_even(4)  # fine
check_if_even('4')  # fine
check_if_even(5.2)  # bug
