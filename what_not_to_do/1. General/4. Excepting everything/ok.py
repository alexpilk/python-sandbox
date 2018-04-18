def divide(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        result = 0
    return result


print(divide(4, 2))  # works fine
print(divide(1, 0))  # excepts fine
print(divide('4', 2))  # raises proper exception
