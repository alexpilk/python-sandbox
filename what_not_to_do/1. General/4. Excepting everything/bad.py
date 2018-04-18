def divide(dividend, divisor):
    try:
        result = dividend / divisor
    except Exception:  # not much better than `4. Excepting everything:`
        result = 0
    return result


print(divide(1, 3))  # works fine
print(divide(1, 0))  # excepts fine
print(divide('4', 2))  # bug - exception should be raised
