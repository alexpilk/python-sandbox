import re


greeting_card = 'My IP is 192.168.1.1, I am a local machine'
regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

if match := regex.search(greeting_card):
    print(match.group())
