import unittest

from src.exceptions.grid_exceptions import OutOfGridBoundsError
from src.grid.grid import BasicGrid, GridBounds
from src.snake import UnclePy


class TestGridStructures(unittest.TestCase):
    def setUp(self):
        self.cell_height = 6
        self.cell_width = 6
        self.margin = 1
        self.cells_in_row = self.cells_in_column = 60

        self.grid = BasicGrid(
            grid_info=(self.cell_height, self.cell_width, self.margin),
            grid_bounds=GridBounds(self.cells_in_row, self.cells_in_column)
        )


class BasicGridTest(unittest.TestCase):
    def setUp(self):
        self.cell_height = 6
        self.cell_width = 6
        self.margin = 1
        self.cells_in_row = self.cells_in_column = 60

        self.grid = BasicGrid(
            grid_info=(self.cell_height, self.cell_width, self.margin),
            grid_bounds=GridBounds(self.cells_in_row, self.cells_in_column)
        )

    def test_draw(self):
        self.assertTrue(True)

    def test_calculate_screen_size(self):
        screen_width = self.cells_in_row * (self.cell_width + self.margin) + self.margin
        screen_height = self.cells_in_column * (self.cell_height + self.margin) + self.margin

        self.assertListEqual([screen_width, screen_height], self.grid.screen_size())

    def test_owner_cells(self):
        self.grid.cells[0].owner = None

        self.assertEqual(len(self.grid.get_owner_cells(None)), 1)

    def test_foreign_cells(self):
        self.grid.cells[0].owner = None

        self.assertEqual(len(self.grid.get_foreign_cells(None)), len(self.grid.cells) - 1)

    def test_clear(self):
        snake = UnclePy(self.grid, (255, 0, 0), 60)
        self.grid.structures.append(snake)
        self.assertTrue(len(self.grid.get_owner_cells(snake)) > 0)

        self.grid.clear()
        self.assertEqual(len(self.grid.get_owner_cells(snake)), 0)


class TestCoordinateConversion(unittest.TestCase):
    def setUp(self):
        self.cell_height = 6
        self.cell_width = 6
        self.margin = 1
        self.cells_in_row = self.cells_in_column = 60

        self.grid = BasicGrid(
            grid_info=(self.cell_height, self.cell_width, self.margin),
            grid_bounds=GridBounds(self.cells_in_row, self.cells_in_column)
        )

    def test_success_conversion(self):
        self.assertTupleEqual((0, 0), self.grid.to_grid_coordinates(self.cell_height - 1, self.cell_width - 1))

    def test_convert_between_cells(self):
        with self.assertRaises(OutOfGridBoundsError):
            if self.margin > 0:
                self.grid.to_grid_coordinates(self.margin - 1, self.margin - 1)

    def test_convert_negative(self):
        with self.assertRaises(OutOfGridBoundsError):
            self.grid.to_grid_coordinates(-5, -20)

    def test_convert_zeros(self):
        with self.assertRaises(OutOfGridBoundsError):
            self.grid.to_grid_coordinates(0, 0)
