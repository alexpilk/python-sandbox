fruits = ['Apples', 'Oranges', 'Bananas', 'Strawberries', 'Raspberries']

for i in range(len(fruits)):
    if str('rr') in fruits[i]:
        raise Exception('rr in fruits!')
