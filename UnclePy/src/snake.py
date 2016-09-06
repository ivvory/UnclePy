from exceptions.bounds import OutOfCellsBoundError
from exceptions.direction import IncorrectMoveDirection
from exceptions.twist import SnakeTwistedError

from UnclePy.src.exceptions.speednegative import SpeedIsNotPositiveException


class UnclePy:
    def __init__(self, grid, color, fps, speed=1):
        self.__grid = grid
        self.__color = color
        self.__fps = fps
        self.__occupied_coordinates = []
        self.__direction = 'RIGHT'
        self.__speed = speed  # speed measures in cells per second
        self.__frames_counter = 0

        #  Dispose the snake in the top left corner of the grid
        self.occupy_cell(0, 0)
        self.occupy_cell(1, 0)
        self.occupy_cell(2, 0)
        self.occupy_cell(3, 0)
        self.occupy_cell(4, 0)
        self.occupy_cell(5, 0)
        self.occupy_cell(6, 0)

    def move(self):
        """
        Move the snake to setting direction

        :return: None
        """

        if self.__frames_counter < (self.__fps - 1) / self.speed:
            self.__frames_counter += 1
            return

        # reset occupied cells color to default
        self.__set_occupied_cells_color((0, 0, 0))

        self.__frames_counter = 0

        old_head = list(self.get_head())
        new_head = old_head.copy()
        if self.direction == 'RIGHT':
            new_head[0] += 1
        elif self.direction == 'LEFT':
            new_head[0] -= 1
        elif self.direction == 'UP':
            new_head[1] -= 1
        elif self.direction == 'DOWN':
            new_head[1] += 1
        else:
            raise IncorrectMoveDirection('')

        if self.__grid.is_cell_coordinates_out_of_grid(new_head[0], new_head[1]):
            raise OutOfCellsBoundError('')

        if tuple(new_head) in self.__occupied_coordinates and tuple(new_head) != self.__occupied_coordinates[0]:
            raise SnakeTwistedError('')

        self.__occupied_coordinates.append(tuple(new_head))
        self.__occupied_coordinates.pop(0)

        self.__set_occupied_cells_color(self.__color)

    def get_head(self):
        """
        :return: tuple of the coordinates of the snake's head
        """

        return self.occupied_coordinates[-1]

    @property
    def occupied_coordinates(self):
        """
        :return: the list of coordinates occupying by the snake
        """

        return self.__occupied_coordinates.copy()

    @property
    def direction(self):
        """
        Return the direction where will the snake move

        :return: string
        """

        return self.__direction

    @direction.setter
    def direction(self, new_direction):
        """
        Set the direction where will the snake move

        :param new_direction: string
        :return: None
        """

        self.__direction = new_direction

    @property
    def speed(self):
        """
        Return the speed for snake's movement

        :return: int
        """

        return self.__speed

    @speed.setter
    def speed(self, speed):
        """
        Set the speed for snake's movement

        :param speed: float
        :return: None
        """

        if speed <= 0:
            raise SpeedIsNotPositiveException('Speed must to be greater than 0')

        self.__speed = speed

    def get_available_cells(self, cell_x, cell_y):
        """
        Find available cells around passing cell.

        :param cell_x: x coordinate of the cell
        :param cell_y: y coordinate of the cell
        :return: tuple of cell coordinates
        """

        cells = set()

        if self.__is_cell_available(cell_x - 1, cell_y):
            cells = cells | {(cell_x - 1, cell_y)}
        if self.__is_cell_available(cell_x, cell_y - 1):
            cells |= {(cell_x, cell_y - 1)}
        if self.__is_cell_available(cell_x + 1, cell_y):
            cells |= {(cell_x + 1, cell_y)}
        if self.__is_cell_available(cell_x, cell_y + 1):
            cells |= {(cell_x, cell_y + 1)}

        return cells

    def __is_cell_available(self, cell_x, cell_y):
        if not self.__grid.is_cell_coordinates_out_of_grid(cell_x, cell_y) and (
         cell_x, cell_y) not in self.__occupied_coordinates:
            return True

        return False

    def occupy_cell(self, cell_x, cell_y):
        """
        Mark that snake occupies passing cell.

        :param cell_x: x coordinate of the cell
        :param cell_y: y coordinate of the cell
        :return: True if passing cell is not occupied yet or not out of grid bounds
        """

        if self.__grid.is_cell_coordinates_out_of_grid(cell_x, cell_y):
            return False

        self.__occupied_coordinates.append((cell_x, cell_y))
        return True

    def __set_occupied_cells_color(self, color):
        for cell in self.__occupied_coordinates:
            self.__grid.set_color_of_cell(color, cell[0], cell[1])
