class TotallyUnexpectedException(Exception):
    pass


try:
    # lots of code
    raise TotallyUnexpectedException
    # lots of code
except TotallyUnexpectedException:
    undefined_function()
