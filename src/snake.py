from src.exceptions.grid_exceptions import OutOfGridBoundsError
from src.exceptions.snake_exceptions import SnakeTwistedError, SnakeHeadBeatenError
from src.exceptions.snake_exceptions import SpeedIsNotPositiveException
from src.grid.cell import GridCell
from src.grid.grid import BasicGrid
from src.grid.structure import GridStructure


class Directions:
    LEFT = 'Left'
    UP = 'Up'
    RIGHT = 'Right'
    DOWN = 'Down'


class UnclePy(GridStructure):
    """
        Class represents a snake on the screen and provides the reins for
        its management.
    """

    def __init__(self, grid: BasicGrid, color: tuple, fps: int, speed=1):
        """
        Declare required variables and dispose the snake on the screen.

        Args:
            grid: grid where snake will be places.
            color: color of the snake on the screen.
            fps: frequency of screen refreshing.
            speed (:obj:`int`, optional): Speed of the snake on the screen.
        """

        #  Dispose the snake in the top left corner of the grid
        coordinates = [(i, 0) for i in range(7)]
        super().__init__(grid, grid.get_cells(coordinates), color)

        self.fps = fps
        self._speed = speed

        self.direction = Directions.RIGHT
        self.frame_counter = 0
        """int: counts how many times a move() method was called to manage a speed of the snake."""

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

    @speed.setter
    def speed(self, speed):
        if speed <= 0:
            raise SpeedIsNotPositiveException('Speed must be greater than 0.')

        self.speed = speed

    def move(self):
        """
        Moves the snake according to the current direction and speed.

        Uses `self.counter` and `self.fps` to imitate the speed.

        Raises:
            SnakeHeadBeatenError: if coordinates of a new head goes beyond the
                borders of the grid.
            SnakeTwistedError: if new head is one the snake cells.
        """

        if self.frame_counter < (self.fps - 1) / self.speed:
            self.frame_counter += 1
            return

        self.frame_counter = 0

        try:
            self.move_head()
        except OutOfGridBoundsError:
            raise SnakeHeadBeatenError()
        except SnakeTwistedError:
            raise

        self.move_tail()

    def move_head(self):
        """Move the head to another cell according current direction."""

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

        new_head.occupy(self)

    def move_tail(self):
        """Release previous tail cell and return it back to the grid."""

        thrown_tail = self.cells[0]
        self.grid.bring_back_cells([thrown_tail])
