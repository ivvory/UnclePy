import unittest

from src.exceptions.snake_exceptions import SnakeTwistedError, SnakeHeadBeatenError
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

    def test_normal_move(self):
        self.snake.move()

    def test_edge_move(self):
        self.snake.direction = Directions.UP
        with self.assertRaises(SnakeHeadBeatenError):
            self.snake.move()

    def test_twisted_move(self):
        self.snake.direction = Directions.DOWN
        self.snake.move()
        self.snake.direction = Directions.LEFT
        self.snake.move()

        self.snake.direction = Directions.UP
        with self.assertRaises(SnakeTwistedError):
            self.snake.move()

    def test_update_head(self):
        self.snake.move_head()
        self.assertEqual(self.snake.cells[-1].coordinates, (7, 0))

    def test_update_tail(self):
        self.snake.move_tail()
        self.assertEqual(self.snake.cells[0].coordinates, (1, 0))
        self.assertFalse(self.grid.get_cell(0, 0).owner is self.snake)
