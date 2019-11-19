

class Spaceship:

    def __init__(self, direction):
        self.direction = direction

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        self.turn_left()
        self.turn_left()
        self.turn_left()
