class BoxNotOpen(Exception):
    pass


class Box:

    def __init__(self):
        self.items = []
        self.is_open = False

    def open(self):
        self.is_open = True
        print('Box opened!')

    def close(self):
        self.is_open = False
        print('Box closed!')

    def put(self, item):
        if not self.is_open:  # repeated code!
            raise BoxNotOpen('Open the Box before using it')
        self.items.append(item)
        print('Put {} into the box'.format(item))

    def remove(self, item):
        if not self.is_open:  # repeated code!
            raise BoxNotOpen('Open the Box before using it')
        self.items.remove(item)
        print('Removed {} from the box'.format(item))


if __name__ == '__main__':
    my_box = Box()
    my_box.open()
    my_box.put('hat')
    my_box.put('shoe')
    my_box.remove('hat')
    my_box.close()
