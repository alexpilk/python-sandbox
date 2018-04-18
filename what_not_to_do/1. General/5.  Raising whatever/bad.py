def check_if_even(number):
    if number % 2 == 1:
        raise Exception('Number is not even!')


try:
    check_if_even('4')  # bug, exception should be raised, 'not even' is printed instead
    print('even!')
except Exception:  # no other choice :(
    print('not even!')
