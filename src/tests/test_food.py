import unittest

from src.exceptions.snake_exceptions import SnakeTwistedError, SnakeHeadBeatenError
from src.food import Food
from src.grid.grid import BasicGrid, GridBounds
from src.snake import UnclePy, Directions


class TestUnclePy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cell_height = 6
        cls.cell_width = 6
        cls.margin = 1
        cls.cells_in_row = cls.cells_in_column = 60

        cls.snake_color = (255, 0, 0)
        cls.fps = 1

    def setUp(self):
        self.grid = BasicGrid(
            grid_info=(self.cell_height, self.cell_width, self.margin),
            grid_bounds=GridBounds(self.cells_in_row, self.cells_in_column),
        )
        self.snake = UnclePy(self.grid, self.snake_color, self.fps)
        self.food = Food(self.grid, (0, 255, 0))

    def test_(self):
        previous_tail = self.snake.tail
        self.snake.move()
        self.assertIs(previous_tail, self.snake.tail)
