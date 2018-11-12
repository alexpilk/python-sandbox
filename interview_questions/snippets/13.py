fruits = ['Apples', 'Oranges', 'Bananas', 'Strawberries', 'Raspberries']

fruits_with_g = []

for i in range(len(fruits)):
    if i % 2 == 1 and str('g') in fruits[i]:
        fruits_with_g.append(fruits[i])

print(fruits_with_g)
