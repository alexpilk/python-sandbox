def split(string: str, index: int) -> tuple:
    return string[:index], string[index:]


chunks = split(5, 'Apple')
chunks.sort()
