import pytest


class EndTerrainException(Exception):
    pass


class Sonda():

    TURN_DIRECTIONS = {
        'N': {'L': 'W', 'R': 'E'},
        'W': {'L': 'S', 'R': 'N'},
        'S': {'L': 'E', 'R': 'W'},
        'E': {'L': 'N', 'R': 'S'}
    }

    MOVE_FORWARD_COORDINATES = {
        'N': {'x':  0, 'y':  1},
        'S': {'x':  0, 'y': -1},
        'E': {'x':  1, 'y':  0},
        'W': {'x': -1, 'y':  0}
    }

    def __init__(self, terrain_limit, start_coordinate, direction):
        self._terrain_limit_x, self._terrain_limit_y = terrain_limit
        self._x, self._y = start_coordinate
        self.direction = direction

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0 or value > self._terrain_limit_x:
            raise EndTerrainException(
                f'X value must be between 0 and {self._terrain_limit_x}')
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0 or value > self._terrain_limit_y:
            raise EndTerrainException(
                f'Y value must be between 0 and {self._terrain_limit_y}')
        self._y = value

    def move_forward(self):
        self.x += self.MOVE_FORWARD_COORDINATES[self.direction]['x']
        self.y += self.MOVE_FORWARD_COORDINATES[self.direction]['y']

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


#==== Tests Sonda ======

def test_move_forward_from_north():
    sonda = Sonda((5, 5), (1, 2), 'N')
    sonda.move_forward()
    assert (sonda.x, sonda.y) == (1, 3)


def test_raise_exception_when_try_move_out_terrain_width():
    sonda = Sonda((5, 5), (1, 2), 'N')
    with pytest.raises(EndTerrainException):
        sonda.x = 6


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
