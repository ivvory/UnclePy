import unittest

from src.food import Food
from src.grid.grid import BasicGrid, GridBounds
from src.snake import UnclePy


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
        self.snake = self.snake = UnclePy(
            self.grid,
            self.grid.get_cell(0, 0),
            7,
            self.snake_color,
            self.fps
        )
        self.food = Food(self.grid, self.grid.get_cell(7, 0), (0, 255, 0), 1)

    def test_eat(self):
        previous_tail = self.snake.tail
        self.snake.move()
        self.assertIs(previous_tail, self.snake.tail)
