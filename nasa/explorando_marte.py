import pytest


class EndTerrainException(Exception):
    pass


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '{} {}'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

class Sonda():

    TURN_DIRECTIONS = {
        'N': {'L': 'W', 'R': 'E'},
        'W': {'L': 'S', 'R': 'N'},
        'S': {'L': 'E', 'R': 'W'},
        'E': {'L': 'N', 'R': 'S'}
    }

    MOVE_FORWARD_COORDINATES = {
        'N': Coordinate(0,  1),
        'S': Coordinate(0, -1),
        'E': Coordinate(1,  0),
        'W': Coordinate(-1, 0)
    }

    def __init__(self, terrain_limit, initial_coordinate, direction):
        self._terrain_limit_x, self._terrain_limit_y = terrain_limit
        self._coordinate = Coordinate(*initial_coordinate)
        self.direction = direction

    @property
    def x(self):
        return self.coordinate.x

    @property
    def y(self):
        return self.coordinate.y

    @property
    def coordinate(self):
        return self._coordinate

    @coordinate.setter
    def coordinate(self, new_coordinate):
        if new_coordinate.x < 0 or new_coordinate.x > self._terrain_limit_x:
            raise EndTerrainException(
                f'X value must be between 0 and {self._terrain_limit_x}')
        if new_coordinate.y < 0 or new_coordinate.y > self._terrain_limit_y:
            raise EndTerrainException(
                f'Y value must be between 0 and {self._terrain_limit_y}')
        self._coordinate = new_coordinate

    def move_forward(self):
        self.coordinate += self.MOVE_FORWARD_COORDINATES[self.direction]

    def turn_left(self):
        self.direction = self.TURN_DIRECTIONS[self.direction]['L']

    def turn_right(self):
        self.direction = self.TURN_DIRECTIONS[self.direction]['R']

    def __repr__(self):
        return f'{self.x} {self.y} {self.direction}'

    def __str__(self):
        return f'{self.x} {self.y} {self.direction}'


class Controller():

    def __init__(self, sonda):
        self.sonda = sonda
        self.courotine = self.courotine_controller()
        next(self.courotine)

    def change_sonda(self, sonda):
        self.sonda = sonda

    def send(self, data):
        self.courotine.send(data)

    def process_movements(self, movements):
        for m in movements:
            self.move(m)

    def move(self, movement):
        possible_moviments = {
            'M': 'move_forward',
            'L': 'turn_left',
            'R': 'turn_right'
        }
        getattr(self.sonda, possible_moviments[movement])()

    def courotine_controller(self):
        while True:
            movement = yield (self.sonda.x, self.sonda.y, self.sonda.direction)
            self.move(movement)


#=== Tests Coordinate ===

def test_sum():
    c1 = Coordinate(1, 2)
    c2 = Coordinate(3, 4)
    assert (c1 + c2) == Coordinate(4, 6)

def test_equality():
    assert Coordinate(1, 2) == Coordinate(1, 2)
    assert not Coordinate(1, 2) == Coordinate(2, 2)

#==== Tests Sonda ======

def test_move_forward_from_north():
    sonda = Sonda((5, 5), (1, 2), 'N')
    sonda.move_forward()
    assert (sonda.x, sonda.y) == (1, 3)


def test_raise_exception_when_try_move_out_terrain_width():
    sonda = Sonda((5, 5), (1, 2), 'N')
    with pytest.raises(EndTerrainException):
        sonda.coordinate = Coordinate(6, 2)


def test_raise_exception_when_try_move_out_terrain_height():
    sonda = Sonda((5, 5), (1, 2), 'N')
    with pytest.raises(EndTerrainException):
        sonda.coordinate = Coordinate(2, 6)


def test_move_forward_from_east():
    sonda = Sonda((5, 5), (1, 2), 'E')
    sonda.move_forward()
    assert (sonda.x, sonda.y) == (2, 2)


def test_move_forward_from_south():
    sonda = Sonda((5, 5), (1, 2), 'S')
    sonda.move_forward()
    assert (sonda.x, sonda.y) == (1, 1)


def test_move_forward_from_west():
    sonda = Sonda((5, 5), (1, 2), 'W')
    sonda.move_forward()
    assert (sonda.x, sonda.y) == (0, 2)


def test_turn_direction_from_north_to_left():
    sonda = Sonda((5, 5), (1, 2), 'N')
    sonda.turn_left()
    assert sonda.direction == 'W'


def test_turn_direction_from_east_to_left():
    sonda = Sonda((5, 5), (1, 2), 'E')
    sonda.turn_left()
    assert sonda.direction == 'N'


def test_turn_direction_from_south_to_left():
    sonda = Sonda((5, 5), (1, 2), 'S')
    sonda.turn_left()
    assert sonda.direction == 'E'


def test_turn_direction_from_west_to_left():
    sonda = Sonda((5, 5), (1, 2), 'W')
    sonda.turn_left()
    assert sonda.direction == 'S'


def test_turn_direction_from_north_to_right():
    sonda = Sonda((5, 5), (1, 2), 'N')
    sonda.turn_right()
    assert sonda.direction == 'E'


def test_turn_direction_from_east_to_right():
    sonda = Sonda((5, 5), (1, 2), 'E')
    sonda.turn_right()
    assert sonda.direction == 'S'


def test_turn_direction_from_south_to_right():
    sonda = Sonda((5, 5), (1, 2), 'S')
    sonda.turn_right()
    assert sonda.direction == 'W'


def test_turn_direction_from_west_to_right():
    sonda = Sonda((5, 5), (1, 2), 'W')
    sonda.turn_right()
    assert sonda.direction == 'N'

#=== Tests controller ====


def test_change_sonda():
    sonda = Sonda((5, 5), (1, 2), 'N')
    controller = Controller(sonda)
    assert controller.sonda == sonda
    sonda2 = Sonda((5, 5), (1, 3), 'N')
    controller.change_sonda(sonda2)
    assert controller.sonda == sonda2


def test_send():
    sonda = Sonda((5, 5), (1, 2), 'N')
    controller = Controller(sonda)
    controller.send('M')
    assert str(sonda) == '1 3 N'


def test_move_turning_direction():
    sonda = Sonda((5, 5), (1, 2), 'N')
    controller = Controller(sonda)
    controller.move('L')
    assert str(sonda) == '1 2 W'


def test_move_forward():
    sonda = Sonda((5, 5), (1, 2), 'N')
    controller = Controller(sonda)
    controller.move('M')
    assert str(sonda) == '1 3 N'


def test_process_movements():
    sonda = Sonda((5, 5), (1, 2), 'N')
    controller = Controller(sonda)
    controller.process_movements("LMLMLMLMM")
    assert repr(sonda) == "1 3 N"
    sonda = Sonda((5, 5), (3, 3), 'E')
    controller = Controller(sonda)
    controller.process_movements("MMRMMRMRRM")
    assert repr(sonda) == "5 1 E"


if __name__ == "__main__":
    pytest.main([__file__, "-k", "test_", "-v", "-s"])
