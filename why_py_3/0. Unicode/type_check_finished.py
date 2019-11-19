from future.builtins import str


def catch_strings(possible_string):
    """
    :param str possible_string:  
    """
    if isinstance(possible_string, str) or isinstance(possible_string, bytes):
        print('Caught!')
    else:
        print('Not a string')


catch_strings('a')
catch_strings(u'a')
catch_strings(4)
