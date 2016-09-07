from exceptions.bounds import OutOfCellsBoundError


class BasicGrid:

    def __init__(self, height, width, margin, cells_in_row, default_color=(0, 0, 0)):
        self.__cell_height = height
        self.__cell_width = width
        self.__margin = margin
        self.__cells_in_row = self.__cells_in_column = cells_in_row
        self.__default_color = default_color

        self.__grid = self.__grid_init()

    def draw(self, screen, pygame):
        """
        Draws the grid on the screen using pygame object.

        :param screen: object of the screen
        :param pygame: object of the pygame module
        :return: None
        """

        for row in range(self.__cells_in_row):
            for column in range(self.__cells_in_column):
                pygame.draw.rect(screen,
                                 self.__grid[row][column],
                                 [(self.__margin + self.__cell_width) * row + self.__margin,
                                  (self.__margin + self.__cell_height) * column + self.__margin,
                                  self.__cell_width,
                                  self.__cell_height])

    def set_color_of_cell(self, color, x, y):
        """
        Set the color of the cell with coordinates x and y.

        :param color: tuple meaning the color in RGB format
        :param x: x coordinate of setting cell
        :param y: y coordinate of setting cell
        :return: None
        """

        self.__grid[x][y] = color

    def calculate_screen_size(self):
        """
        Calculates the coordinates of the screen to be initialized using the margin
        between cells, width and height of each cell and count of cells in row/column
        as well.

        :return: the list of calculated screen coordinates
        """

        width = self.__margin + self.__cells_in_row * (self.__cell_width + self.__margin)
        height = self.__margin + self.__cells_in_row * (self.__cell_height + self.__margin)

        return [width, height]

    def clear(self):
        """
        Set all cells in the grid to default color.

        :return: None
        """

        for row in self.__grid:
            for cell in row:
                cell = self.default_color

    def __grid_init(self):
        """
        Creates 2-dimensional array contained the color of each cell in the grid
        and init all cells by default color (BLACK).

        :return: 2-dimensional array of default colours
        """

        grid = [[self.__default_color for x in range(self.__cells_in_row)] for y in range(self.__cells_in_row)]

        return grid

    def convert_to_cell_coordinates(self, x, y):
        """
        Converts screen coordinates to the coordinates of the cell in the grid.

        :return tuple of cell coordinates
        """

        x_remainder = x % (self.__cell_width + self.__margin)
        y_remainder = y % (self.__cell_width + self.__margin)

        if x_remainder < self.__margin or y_remainder < self.__margin:
            raise OutOfCellsBoundError("Passing coordinates are between cells.")
        if x < 0 or y < 0:
            raise OutOfCellsBoundError("Passing coordinates are negative.")

        cell_x = int(x / (self.__cell_width + self.__margin))
        cell_y = int(y / (self.__cell_width + self.__margin))

        return cell_x, cell_y

    def get_color_of_cell(self, x, y):
        """
        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        :return: tuple in RGB format
        """

        return self.__grid[x][y]

    def get_grid(self):
        return self.__grid

    def is_cell_coordinates_out_of_grid(self, cell_x, cell_y):
        """
        :param cell_x: x coordinate of the cell
        :param cell_y: y coordinate of the cell
        :return: True if coordinates are out of grid else False
        """

        if cell_x < 0 or cell_y < 0 or cell_x >= self.__cells_in_row or cell_y >= self.__cells_in_column:
            return True

        return False

    @property
    def default_color(self):
        """
        Return default color of a grid

        :return: color as tuple
        """

        return self.__default_color

    @default_color.setter
    def default_color(self, new_color):
        """
        Set default color of a grid

        :param new_color: color as tuple
        :return: None
        """

        self.__default_color = new_color
