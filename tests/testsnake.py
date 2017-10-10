import unittest

from src.basicgrid import BasicGrid
from src.snake import UnclePy
from src.exceptions.snake_exceptions import IncorrectMoveDirection
from src.exceptions.snake_exceptions import SnakeTwistedError
from src.exceptions.grid_exceptions import OutOfCellsBoundError


class TestUnclePy(unittest.TestCase):
    def setUp(self):
        self.cell_height = 6
        self.cell_width = 6
        self.margin = 1
        self.cells_in_row = self.cells_in_column = 60

        self.grid = BasicGrid(self.cell_height, self.cell_width, self.margin, self.cells_in_row)

        self.snake_color = (255, 0, 0)
        self.fps = 2
        self.snake = UnclePy(self.grid, self.snake_color, self.fps)

    def test_move(self):
        this = self

        def move(direction):
            this.snake.direction = direction
            for i in range(self.fps):
                this.snake.move()

        try:
            move('Incorrect direction')
        except IncorrectMoveDirection:
            pass  # All right
        else:
            self.fail('Method does not fail when direction is incorrect')

        try:
            move('UP')
        except OutOfCellsBoundError:
            pass  # All right
        else:
            self.fail('Method does not fail when snake is out of grid')

        old_head = list(self.snake.get_head())

        sequence_of_directions = ['RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP']
        [move(direction) for direction in sequence_of_directions]

        new_head = list(self.snake.get_head())
        old_head[1] += 1
        self.assertListEqual(new_head, old_head)

        try:
            move('UP')
        except SnakeTwistedError:
            pass  # All right
        else:
            self.fail('Method does not fail when snake is twisted')
