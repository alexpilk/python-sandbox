class BoxInaccessible(Exception):
    pass


def require_open(method):
    def wrapper(self, *args, **kwargs):
        if not self.is_open:
            raise BoxInaccessible('Open the Box before using it')
        return method(self, *args, **kwargs)
    return wrapper


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

    @require_open
    def put(self, item):
        self.items.append(item)
        print('Put {} into the box'.format(item))

    @require_open
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
