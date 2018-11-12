try:
    5 / 0
except Exception as e:
    print("Exception")
    raise Exception(e)
except ZeroDivisionError as e:
    print("ZeroDivisionError")
