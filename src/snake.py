from src.exceptions.grid_exceptions import OutOfCellsBoundError
from src.exceptions.snake_exceptions import IncorrectMoveDirection
from src.exceptions.snake_exceptions import SnakeTwistedError
from src.exceptions.snake_exceptions import SpeedIsNotPositiveException


class Directions:
    LEFT = 'Left'
    UP = 'Up'
    RIGHT = 'Right'
    DOWN = 'Down'


class UnclePy:
    """
        Class represents a snake on the screen and provides the reins for
        its management.
    """

    def __init__(self, grid, color, fps, speed=1):
        """
        Declare required variables and dispose the snake on the screen.

        Args:
            grid (:obj:`BasicGrid`): Object of the grid containing.
            color (:obj:`tuple`): A snake will have such color on the screen.
            fps (:obj:`int`): Frequency of screen refreshing.
            speed (:obj:`int`, optional): Speed of the snake on the screen.
        """
        self.__grid = grid
        self.__color = color
        self.__fps = fps
        self.__speed = speed

        #: list of tuples: containing cells which are occupied by the snake.
        self.__occupied_coordinates = []

        self.__direction = Directions.RIGHT
        self.__frames_counter = 0
        """int: counts how many times a move() method was called to manage a speed of the snake."""

        #  Dispose the snake in the top left corner of the grid
        self._occupy_cell(0, 0)
        self._occupy_cell(1, 0)
        self._occupy_cell(2, 0)
        self._occupy_cell(3, 0)
        self._occupy_cell(4, 0)
        self._occupy_cell(5, 0)
        self._occupy_cell(6, 0)

    def move(self):
        """
        Moves the snake according to setting direction and speed.

        Uses self.counter and self.fps for imitation of speed. self.direction
        indicates which direction will use. Moving means changing the list of
        occupying coordinates, namely adds new head cell which becomes a new
        head and remove the tail deleting it from the occupying cells list. If
        such moving is not possible the exception will be thrown.

        Raises:
            OutOfCellsBoundError: if coordinates of a new head goes beyond the
            borders of the grid.
            SnakeTwistedError: if the snake still have contained coordinates of
            a new head.

        Returns:
            :obj:`None`.
        """

        if self.__frames_counter < (self.__fps - 1) / self.speed:
            self.__frames_counter += 1
            return

        # reset occupied cells color to default
        self._set_occupied_cells_color((0, 0, 0))

        self.__frames_counter = 0

        old_head = list(self.get_head())
        new_head = old_head.copy()
        if self.direction == Directions.RIGHT:
            new_head[0] += 1
        elif self.direction == Directions.LEFT:
            new_head[0] -= 1
        elif self.direction == Directions.UP:
            new_head[1] -= 1
        elif self.direction == Directions.DOWN:
            new_head[1] += 1
        else:
            raise IncorrectMoveDirection('')

        if self.__grid.is_coordinates_out_of_grid(new_head[0], new_head[1]):
            raise OutOfCellsBoundError('The snake has moved beyond the grid borders')

        if tuple(new_head) in self.__occupied_coordinates and tuple(new_head) != self.__occupied_coordinates[0]:
            raise SnakeTwistedError('')

        self.__occupied_coordinates.append(tuple(new_head))
        self.__occupied_coordinates.pop(0)

        self._set_occupied_cells_color(self.__color)

    def get_head(self):
        """
        Get the head of the snake.

        Returns:
            :obj:`tuple`: a head of the snake.
        """

        return self.occupied_coordinates[-1]

    @property
    def occupied_coordinates(self):
        """:obj:`list` of :obj:`str`: coordinates occupying by the snake."""

        return self.__occupied_coordinates.copy()

    @property
    def direction(self):
        """str: the direction where the snake is moving."""

        return self.__direction

    @direction.setter
    def direction(self, new_direction):
        self.__direction = new_direction

    @property
    def speed(self):
        """int: speed of the snake's movement."""

        return self.__speed

    @speed.setter
    def speed(self, speed):
        if speed <= 0:
            raise SpeedIsNotPositiveException('Speed must be greater than 0.')

        self.__speed = speed

    def get_available_cells(self, cell_x, cell_y):
        """
        Find available cells around the passing cell.

        Args:
            cell_x: x coordinate of the cell.
            cell_y: y coordinate of the cell.

        Returns:
            Set of tuples which are nearest cell around the passing cell.
        """

        cells = set()

        if self._is_cell_available(cell_x - 1, cell_y):
            cells = cells | {(cell_x - 1, cell_y)}
        if self._is_cell_available(cell_x, cell_y - 1):
            cells |= {(cell_x, cell_y - 1)}
        if self._is_cell_available(cell_x + 1, cell_y):
            cells |= {(cell_x + 1, cell_y)}
        if self._is_cell_available(cell_x, cell_y + 1):
            cells |= {(cell_x, cell_y + 1)}

        return cells

    def _is_cell_available(self, cell_x, cell_y):
        if not self.__grid.is_coordinates_out_of_grid(cell_x, cell_y) and (
         cell_x, cell_y) not in self.__occupied_coordinates:
            return True

        return False

    def _occupy_cell(self, cell_x, cell_y):

        if self.__grid.is_coordinates_out_of_grid(cell_x, cell_y):
            return False

        self.__occupied_coordinates.append((cell_x, cell_y))
        return True

    def _set_occupied_cells_color(self, color):
        for cell in self.__occupied_coordinates:
            self.__grid.set_color_of_cell(color, cell[0], cell[1])
