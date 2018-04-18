from future.utils import raise_with_traceback


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

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.closse()  # intentional typo to trigger exception in __exit__
        except Exception as e:
            raise_with_traceback(e, exc_tb)  # restores original traceback in Python 2


if __name__ == '__main__':
    with Box() as box:
        box.remove('whatever')
        print('About to exit')
