class BoxInaccessible(Exception):
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
        self.items.remove(item)
        print('Removed {} from the box'.format(item))


if __name__ == '__main__':
    my_box = Box()
    my_box.open()
    my_box.put('hat')
    my_box.put('shoe')
    my_box.remove('hat')
    my_box.close()
