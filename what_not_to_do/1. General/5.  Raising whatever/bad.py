def check_if_even(number):
    if number % 2 == 1:
        raise Exception('Number is not even!')


try:
    check_if_even('4')  # bug
    print('even!')
except Exception:
    print('not even!')
