

class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class TrashCollector:

    def __init__(self):
        self.trash_collected = {}

    def __repr__(self):
        return 'Collected trash {}'.format(self.trash_collected)

    def collect_trash(self, coordinate):
        if coordinate in self.trash_collected:
            self.trash_collected[coordinate] += 1
        else:
            self.trash_collected[coordinate] = 1


trash_collector = TrashCollector()
trash_collector.collect_trash(Coordinate(0, 0))
trash_collector.collect_trash(Coordinate(1, 1))
trash_collector.collect_trash(Coordinate(2, 2))
trash_collector.collect_trash(Coordinate(0, 0))
print(trash_collector)
