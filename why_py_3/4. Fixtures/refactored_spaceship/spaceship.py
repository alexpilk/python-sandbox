DIRECTION_TO_ANGLE = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270
}
ANGLE_TO_DIRECTION = {angle: direction for direction, angle in DIRECTION_TO_ANGLE.items()}


class Spaceship:

    def __init__(self, direction):
        self._angle = DIRECTION_TO_ANGLE[direction]

    @property
    def direction(self):
        return ANGLE_TO_DIRECTION[self._angle]

    @direction.setter
    def direction(self, direction):
        self._angle = DIRECTION_TO_ANGLE[direction]

    def turn_left(self):
        self._angle = (self._angle - 90) % 360
        return self._angle

    def turn_right(self):
        self._angle = (self._angle + 90) % 360
        return self._angle
