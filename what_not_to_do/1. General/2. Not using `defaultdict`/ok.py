from collections import defaultdict


class FreezerItemNotFound(Exception):
    pass


class FoodItem:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return '{name} of size {size}'.format(
            name=self.name,
            size=self.size
        )


class Freezer:
    """
    Stores food in self.food in the following format:

    {
        <FoodItem.name>: [<FoodItem>, <FoodItem>, ...],
        ...
    }
    """
    def __init__(self):
        self.food = defaultdict(list)

    def put(self, item):
        self.food[item.name].append(item)

    def get(self, item_name):
        try:
            return self.food[item_name].pop()
        except IndexError:
            raise FreezerItemNotFound('Item "{}" not found!'.format(item_name))

    def __repr__(self):
        return repr(self.food)


if __name__ == '__main__':
    freezer = Freezer()
    freezer.put(FoodItem('banana', 5))
    print('Freezer: {}'.format(freezer))
    banana = freezer.get('banana')
    print('Banana: {}'.format(banana))
    try:
        orange = freezer.get('orange')
    except FreezerItemNotFound as e:
        print('Expected exception for nonexistent item: {}'.format(e))
