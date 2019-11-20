import random


def random_sequence():
    while True:
        new_number = random.randint(0, 100)
        if new_number % 5 == 0:
            raise StopIteration
        yield new_number


for i in random_sequence():
    print(i)
