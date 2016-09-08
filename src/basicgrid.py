from exceptions.bounds import OutOfCellsBoundError


class BasicGrid:

    def __init__(self, height, width, margin, cells_in_row, default_color=(0, 0, 0)):
        self.cell_height = height
        self.cell_width = width
        self.margin = margin
        self.cells_in_row = self.cells_in_column = cells_in_row

        self._default_color = default_color
        self._grid = self._grid_init()

    def draw(self, screen, pygame):
        """
        Draws the grid on the screen using pygame object.

        :param screen: object of the screen
        :param pygame: object of the pygame module
        :return: None
        """

        for row in range(self.cells_in_row):
            for column in range(self.cells_in_column):
                pygame.draw.rect(screen,
                                 self._grid[row][column],
                                 [(self.margin + self.cell_width) * row + self.margin,
                                  (self.margin + self.cell_height) * column + self.margin,
                                  self.cell_width,
                                  self.cell_height])

    def calculate_screen_size(self):
        """
        Calculates the coordinates of the screen to be initialized using the margin
        between cells, width and height of each cell and count of cells in row/column
        as well.

        :return: the list of calculated screen coordinates
        """

        width = self.margin + self.cells_in_row * (self.cell_width + self.margin)
        height = self.margin + self.cells_in_row * (self.cell_height + self.margin)

        return [width, height]

    def clear(self):
        """
        Set all cells in the grid to default color.

        :return: None
        """

        for row in self._grid:
            for cell in row:
                cell = self.default_color

    def convert_to_cell_coordinates(self, x, y):
        """
        Converts screen coordinates to the coordinates of the cell in the grid.

        :return tuple of cell coordinates
        """

        x_remainder = x % (self.cell_width + self.margin)
        y_remainder = y % (self.cell_width + self.margin)

        if x_remainder < self.margin or y_remainder < self.margin:
            raise OutOfCellsBoundError("Passing coordinates are between cells.")
        if x < 0 or y < 0:
            raise OutOfCellsBoundError("Passing coordinates are negative.")

        cell_x = int(x / (self.cell_width + self.margin))
        cell_y = int(y / (self.cell_width + self.margin))

        return cell_x, cell_y

    def set_color_of_cell(self, color, x, y):
        """
        Set the color of the cell with coordinates x and y.

        :param color: tuple meaning the color in RGB format
        :param x: x coordinate of setting cell
        :param y: y coordinate of setting cell
        :return: None
        """

        cell_coordinates = self.convert_to_cell_coordinates(x, y)
        self._grid[cell_coordinates[0]][cell_coordinates[1]] = color

    def __grid_init(self):
        """
        Creates 2-dimensional array contained the color of each cell in the grid
        and init all cells by default color (BLACK).

        :return: 2-dimensional array of default colours
        """

        grid = [[self._default_color for x in range(self.cells_in_row)] for y in range(self.cells_in_row)]

        return grid

    def __is_cell_coordinates_out_of_grid(self, cell_x, cell_y):
        """
        :param cell_x: x coordinate of the cell
        :param cell_y: y coordinate of the cell
        :return: True if coordinates are out of grid else False
        """

        if cell_x < 0 or cell_y < 0 or cell_x >= self.cells_in_row or cell_y >= self.cells_in_column:
            return True

        return False

    @property
    def _grid(self):
        return self._grid.copy()

    @property
    def _default_color(self):
        """
        Return default color of a grid

        :return: color as tuple
        """

        return self._default_color

    @_default_color.setter
    def _default_color(self, red, green, blue):
        """
        Set default color of a grid

        :param new_color: color as tuple
        :return: None
        """

        self._default_color = (red, green, blue)

# http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
