def to_lowercase(*args, **kwargs):
    return_set = kwargs.pop('return_set', False)
    if return_set:
        return {s.lower() for s in args}
    else:
        return [s.lower() for s in args]


strings = to_lowercase('a', 'B', return_set=True)
print(strings)
