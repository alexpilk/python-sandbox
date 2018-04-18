class BoxInaccessible(Exception):
    pass


class ItemNotFound(Exception):
    pass


class Box:

    def __init__(self):
        self._items = []
        self.accessible = False

    @property
    def items(self):
        if not self.accessible:
            raise BoxInaccessible('Open the Box before using it')
        return self._items

    def open(self):
        self.accessible = True
        print('Box opened!')

    def close(self):
        self.accessible = False
        print('Box closed!')

    def put(self, item):
        self.items.append(item)
        print('Put {} into the box'.format(item))

    def remove(self, item):
        try:
            self.items.remove(item)
            print('Removed {} from the box'.format(item))
        except ValueError:
            raise ItemNotFound('Item "{}" not found in the box'.format(item))
