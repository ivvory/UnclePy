from enum import Enum
from typing import List

from two_d.exceptions.grid_exceptions import OutOfGridBoundsError
from two_d.exceptions.snake_exceptions import SnakeTwistedError, SnakeHeadBeatenError, LongDisposeLengthException
from two_d.food import Food
from two_d.grid.cell import GridCell
from two_d.grid.structure import GridStructure


class Directions(Enum):
    LEFT = 'Left'
    UP = 'Up'
    RIGHT = 'Right'
    DOWN = 'Down'


class UnclePy(GridStructure):
    """
        Class represents a snake on the screen and provides the reins for
        its management.
    """

    def __init__(self, grid, cell, length, color: tuple):
        """
        Declare required variables and dispose the snake on the screen.

        Args:
            grid: grid where snake will be places.
            color: color of the snake on the screen.
        """
        direction = Directions.RIGHT

        super().__init__(grid, [], color)
        discovered_cells = self.get_dispose_cells(cell, length)
        self + discovered_cells

        self.eaten = False
        self.scores = 0

        self._speed = 1
        self._difficulty = 0.01

    @property
    def head(self) -> GridCell:
        """The head cell of the snake."""

        return self.cells[-1]

    @property
    def tail(self) -> GridCell:
        """The tail cell of the snake."""

        return self.cells[0]

    @property
    def speed(self):
        """int: speed of the snake's movement."""

        return self._speed

    def move(self):
        """Move the snake according to the current `direction`.

        Raises:
            SnakeHeadBeatenError: if coordinates of a new head goes beyond the
                borders of the grid.
            SnakeTwistedError: if new head is one the snake cells.
        """
        self.eaten = False

        try:
            self.move_head()
        except OutOfGridBoundsError:
            raise SnakeHeadBeatenError()
        except SnakeTwistedError:
            raise

        if not self.eaten:
            self.move_tail()

        self._speed += self._difficulty
        print(self.speed)

    def move_head(self):
        """Move the head."""

        x, y = self.head.coordinates

        if self.direction == Directions.RIGHT:
            x += 1
        elif self.direction == Directions.LEFT:
            x -= 1
        elif self.direction == Directions.UP:
            y -= 1
        elif self.direction == Directions.DOWN:
            y += 1

        new_head = self.grid.get_cell(x, y)

        if new_head.owner is self:
            raise SnakeTwistedError()

        if isinstance(new_head.owner, Food):
            self.eat(new_head.owner)

        new_head.occupy(self)

    def move_tail(self):
        """Release previous tail cell and return it back to the grid."""

        thrown_tail = self.cells[0]
        self.grid.bring_back_cells([thrown_tail])

    def eat(self, food: Food):
        self.eaten = True
        self.scores += food.value
        self.grid.add_food((0, 0, 255), 2)
        print(f'{food.value} scores added.')

    def get_dispose_cells(self, tail_cell: GridCell, length) -> List[GridCell]:
        """Get cells where the snake will be disposed.

        Note:
            Change `direction` to the one from tail to found head.

        Args:
            tail_cell: future tail.
            length: length of a future snake.

        Returns:
            :obj:`list` of :obj:`GridCell`: Cells to dispose.
        """
        half_grid_x_len = self.grid.bounds.cells_in_row / 2
        half_grid_y_len = self.grid.bounds.cells_in_column / 2

        if length > half_grid_x_len and length > half_grid_y_len:
            raise LongDisposeLengthException()

        all_directions = Directions.RIGHT, Directions.LEFT, Directions.UP, Directions.DOWN
        for d in all_directions:
            cells = self._discover_direction(tail_cell, d, length)

            if cells:
                self.direction = d
                break
        else:
            cells = []

        return [tail_cell] + cells

    def _discover_direction(self, cell, direction, length):
        tail_x, tail_y = cell.coordinates

        if direction == Directions.RIGHT:
            good_dispose_direction = tail_x + length < self.grid.bounds.cells_in_row / 2
        elif direction == Directions.LEFT:
            good_dispose_direction = tail_x - length > self.grid.bounds.cells_in_row / 2
        elif direction == Directions.UP:
            good_dispose_direction = tail_y - length > self.grid.bounds.cells_in_column / 2
        elif direction == Directions.DOWN:
            good_dispose_direction = tail_y + length < self.grid.bounds.cells_in_column / 2

        if not good_dispose_direction:
            return False

        cells = self._get_cells_from(cell, direction, length)

        if not all(self.grid.is_free_cell(c) for c in cells):
            return False

        return cells

    def _get_cells_from(self, cell, direction, count):
        cell_x, cell_y = cell.coordinates

        if direction == Directions.RIGHT:
            cell_coordinates = [(cell_x + i, cell_y) for i in range(1, count)]
        elif direction == Directions.LEFT:
            cell_coordinates = [(cell_x - i, cell_y) for i in range(1, count)]
        elif direction == Directions.UP:
            cell_coordinates = [(cell_x, cell_y - i) for i in range(1, count)]
        elif direction == Directions.DOWN:
            cell_coordinates = [(cell_x, cell_y + i) for i in range(1, count)]

        return self.grid.get_cells(cell_coordinates)
