

def catch_strings(possible_string):
    if isinstance(possible_string, str):
        print('Caught!')
    else:
        print('Not a string')


catch_strings('a')
catch_strings(4)
