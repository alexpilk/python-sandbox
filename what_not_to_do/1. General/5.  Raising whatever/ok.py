class UnevenNumberException(Exception):
    pass


def check_if_even(number):
    if number % 2 == 1:
        raise UnevenNumberException('Number is not even!')


try:
    check_if_even('4')  # raises proper exception
    print('even!')
except UnevenNumberException:
    print('not even!')
