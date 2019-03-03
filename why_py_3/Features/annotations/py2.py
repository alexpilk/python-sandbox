def split(string, index):
    """
    :param str string:
    :param int index:
    :rtype: tuple
    """
    return string[:index], string[index:]


chunks = split(5, 'Apple')
chunks.sort()
