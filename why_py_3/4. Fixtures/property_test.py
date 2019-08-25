class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return "Rectangle with width: {} and height {}".format(
            self.width, self.height
        )

    @property
    def area(self):
        return self.width * self.height


import pytest


@pytest.fixture
def rectangle():
    return Rectangle(1, 1)


def test_rectangle(rectangle):
    rectangle.area = 'whatever'  # correctly fails in Python 3, incorrectly succeeds in Python 2
    print(rectangle.area)
