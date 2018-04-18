class OddNumberException(Exception):
    pass


def check_if_even(number):
    if int(number) % 2 == 1:  # implicit casting to int without a reason!
        raise OddNumberException('Number is not even!')


check_if_even(4)  # fine
check_if_even('4')  # bug - strings cannot be even or odd, so this should raise exception!
check_if_even(5.2)  # bug - 5.2 is even, but int(5.2) = 5, which is odd!
