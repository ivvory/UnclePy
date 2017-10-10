import unittest

from src.basicgrid import BasicGrid
from src.exceptions.grid_exceptions import OutOfCellsBoundError

from src.snake import UnclePy


class BasicGridTest(unittest.TestCase):
    def setUp(self):
        self.cell_height = 6
        self.cell_width = 6
        self.margin = 1
        self.cells_in_row = self.cells_in_column = 60
        self._default_color = (200, 200, 200)

        self.grid = BasicGrid(self.cell_height, self.cell_width, self.margin, self.cells_in_row)

    def test_draw(self):
        self.assertTrue(True)

    def test_set_color_of_cell(self):
        color = (255, 255, 255)

        self.grid.set_color_of_cell(color, 0, 0)
        self.assertTupleEqual(color, self.grid.grid[0][0])

    def test_calculate_screen_size(self):
        screen_width = self.cells_in_row * (self.cell_width + self.margin) + self.margin
        screen_height = self.cells_in_column * (self.cell_height + self.margin) + self.margin

        self.assertListEqual([screen_width, screen_height],
                             self.grid.screen_size())

    def test_clear(self):
        UnclePy(self.grid, (255, 0, 0), 60)
        self.grid.clear()

        for row in self.grid.grid:
            for cell in row:
                self.assertTupleEqual(self.grid.default_color, cell)

    def test_grid_init(self):
        for row in self.grid.grid:
            for cell in row:
                self.assertTupleEqual(self.grid.default_color, cell)

    def test_convert_to_cell_coordinates(self):
        self.assertTupleEqual((0, 0), self.grid.to_grid_coordinates(self.cell_height - 1, self.cell_width - 1))

        try:
            if self.margin > 0:
                self.grid.to_grid_coordinates(self.margin - 1, self.margin - 1)
        except OutOfCellsBoundError:
            pass  # All right
        else:
            self.fail('Method does not fail if passed coordinates are between cells')

        try:
            self.grid.to_grid_coordinates(-5, -20)
        except OutOfCellsBoundError:
            pass  # All right
        else:
            self.fail('Method does not fail if passed coordinates are negative')

        try:
            self.grid.to_grid_coordinates(0, 0)
        except OutOfCellsBoundError:
            pass  # All right
        else:
            self.fail('Method does not fail if passed coordinates are zeros')
