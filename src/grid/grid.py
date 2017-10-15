import itertools
from collections import namedtuple
from datetime import datetime

from src.exceptions.grid_exceptions import OutOfGridBoundsError
from src.grid.cell import GridCell
from src.grid.structure import GridStructure


GridBounds = namedtuple('GridBounds', ['cells_in_row', 'cells_in_column'])


class BasicGrid:
    """
    Represent the grid.
    """

    def __init__(
            self,
            grid_info: tuple,
            grid_bounds: tuple,
    ):
        """
        Initializes grid properties.

        Args:

        """

        self.cell_height, self.cell_width, self.cell_margin = grid_info
        self.bounds = GridBounds(*grid_bounds)
        self.color = (0, 0, 0)
        self.structures = []

        self._cells = self._create_grid_cells()
        self.main_structure = GridStructure(self, self._cells, self.color)

    @property
    def cells(self):
        return self._cells

    def draw(self, screen, pygame):
        """
        Draw the grid on the screen using pygame object.

        Args:
            :obj:`screen`: specified the screen where a snake will be drawn.
            :obj:`pygame`: used to call ``draw`` method.
        """
        for row in range(self.bounds.cells_in_row):
            for column in range(self.bounds.cells_in_column):
                pygame.draw.rect(
                    screen,
                    self.get_cell(row, column).color,
                    [
                        (self.cell_margin + self.cell_width) * row + self.cell_margin,
                        (self.cell_margin + self.cell_height) * column + self.cell_margin,
                        self.cell_width,
                        self.cell_height
                    ]
                )

    def add_structures(self, structures: list):
        self.structures += structures

    def get_owner_cells(self, owner: GridStructure) -> list:
        return [c for c in self.cells if c.owner is owner]

    def get_foreign_cells(self, owner: GridStructure) -> list:
        return [c for c in self.cells if c.owner is not owner]

    def get_cell(self, grid_x: int, grid_y: int) -> GridCell:
        try:
            cell = next(c for c in self.cells if c.coordinates == (grid_x, grid_y))
        except StopIteration:
            raise OutOfGridBoundsError(f'You cannot get cell with coordinates ({grid_x}, {grid_y}).')

        return cell

    def get_cells(self, coordinates: list) -> list:
        return [self.get_cell(*coord) for coord in coordinates]

    def bring_back_cells(self, cells: list):
        self.main_structure + cells

    def screen_size(self):
        """
        Calculates the screen coordinates according to established grid params.

        Returns:
             :obj:`list`: width and height of the screen in pixels.
        """

        width = self.cell_margin + self.bounds.cells_in_row * (self.cell_width + self.cell_margin)
        height = self.cell_margin + self.bounds.cells_in_row * (self.cell_height + self.cell_margin)

        return [width, height]

    def clear(self):
        """Set all cells in the grid to default color."""

        [c.occupy(self.main_structure) for c in self.cells]

    def to_grid_coordinates(self, screen_x, screen_y):
        """
        Convert screen coordinates to grid coordinates.

        Raises:
            OutOfGridBoundsError: if screen coordinates are negative or between cells.

        Returns:
             :obj:`tuple`: converted cell coordinates.
        """

        x_remainder = screen_x % (self.cell_width + self.cell_margin)
        y_remainder = screen_y % (self.cell_width + self.cell_margin)

        if x_remainder < self.cell_margin or y_remainder < self.cell_margin:
            raise OutOfGridBoundsError("Passing coordinates are between cells.")
        if screen_x < 0 or screen_y < 0:
            raise OutOfGridBoundsError("Passing coordinates are negative.")

        cell_x = int(screen_x / (self.cell_width + self.cell_margin))
        cell_y = int(screen_y / (self.cell_width + self.cell_margin))

        return cell_x, cell_y

    def _create_grid_cells(self):
        x_indices = range(self.bounds.cells_in_row)
        y_indices = range(self.bounds.cells_in_column)
        index_combinations = itertools.product(x_indices, y_indices)
        cells = [GridCell((x, y)) for x, y in index_combinations]

        return cells

# http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html