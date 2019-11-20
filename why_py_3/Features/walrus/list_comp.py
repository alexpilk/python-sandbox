
raw_strings = [' parse me   ', '       data          ', ' looooooong striiiiing']
parsed = [string.strip() for string in raw_strings if len(string.strip()) < 10]
print(parsed)
