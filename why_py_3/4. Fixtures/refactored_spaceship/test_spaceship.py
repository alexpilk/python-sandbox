from spaceship import Spaceship
import pytest


@pytest.fixture
def spaceship():
    return Spaceship(direction='N')


@pytest.mark.parametrize('direction,expected', [
    ('N', 'W'), ('W', 'S'), ('S', 'E'), ('E', 'N')
])
def test_turns_left(spaceship, direction, expected):
    spaceship.direction = direction
    spaceship.turn_left()
    assert spaceship.direction == expected


@pytest.mark.parametrize('direction,expected', [
    ('N', 'E'), ('W', 'N'), ('S', 'W'), ('E', 'S')
])
def test_turns_right(spaceship, direction, expected):
    spaceship.direction = direction
    spaceship.turn_right()
    assert spaceship.direction == expected
