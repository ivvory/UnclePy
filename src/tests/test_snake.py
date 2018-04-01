import unittest

from src.exceptions.snake_exceptions import SnakeTwistedError, SnakeHeadBeatenError, SnakeBackwardMoveError
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

        cls.length = 5
        cls.snake_color = (255, 0, 0)
        cls.fps = 1

    def setUp(self):
        self.grid = BasicGrid(
            grid_info=(self.cell_height, self.cell_width, self.margin),
            grid_bounds=GridBounds(self.cells_in_row, self.cells_in_column),
        )
        self.snake = UnclePy(
            self.grid,
            self.grid.get_cell(self.cells_in_row - self.length + 1, 0),
            self.length,
            self.snake_color,
        )

    def test_normal_move(self):
        self.snake.move()

    def test_edge_move(self):
        self.snake.direction = Directions.UP
        with self.assertRaises(SnakeHeadBeatenError):
            self.snake.move()

    def test_twisted_move(self):
        self.fps = -1
        self.snake.direction = Directions.DOWN
        self.snake.move()
        self.snake.direction = Directions.RIGHT
        self.snake.move()

        self.snake.direction = Directions.UP
        with self.assertRaises(SnakeTwistedError):
            self.snake.move()

    def test_update_head(self):
        self.snake.move_head()
        self.assertEqual(self.snake.cells[-1].coordinates, (51, 0))

    def test_update_tail(self):
        self.snake.move_tail()
        self.assertEqual(self.snake.cells[0].coordinates, (55, 0))
        self.assertFalse(self.grid.get_cell(0, 0).owner is self.snake)

    def test_left_dispose(self):
        assumed_coordinates = {(56, 0), (55, 0), (54, 0), (53, 0), (52, 0)}
        real_coordinates = set(c.coordinates for c in self.snake.cells)
        self.assertSetEqual(real_coordinates, assumed_coordinates)

    def test_direction_setter(self):
        considering_directions = Directions.RIGHT, Directions.LEFT, Directions.DOWN, Directions.UP
        opposite_directions = Directions.LEFT, Directions.RIGHT, Directions.UP, Directions.DOWN

        for prev_d, new_d in zip(opposite_directions, considering_directions):
            self.snake._direction = prev_d
            with self.assertRaises(SnakeBackwardMoveError):
                self.snake.direction = new_d

    def test_available_directions(self):
        should_be_available = [Directions.LEFT, Directions.DOWN]

        self.assertListEqual(list(self.snake.available_directions()), should_be_available)

    def test_food_distance(self):
        head_x, head_y = self.snake.head.coordinates
        nearest_food_cell = self.grid.get_cell(head_x - 4, head_y + 3)
        distant_food_cell = self.grid.get_cell(head_x - 4, head_y + 4)

        Food(self.grid, nearest_food_cell, (50, 50, 50), 1)
        Food(self.grid, distant_food_cell, (50, 50, 50), 1)

        nearest_distance = self.snake.get_food_distance()
        expected_distance = 5.0

        self.assertEqual(nearest_distance, expected_distance)

        self.grid.bring_back_cells([nearest_food_cell])
        new_nearest_distance = self.snake.get_food_distance()
        self.assertGreater(new_nearest_distance, nearest_distance)
