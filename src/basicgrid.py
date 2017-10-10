from src.exceptions.grid_exceptions import OutOfCellsBoundError


class BasicGrid:
    """
    Represent the grid.
    """

    def __init__(self, height, width, margin, cells_in_row):
        """
        Initializes grid properties.

        Args:
            height (:obj:`int`): Height of the cell in pixels.
            width (:obj:`int`): Width of the cell in pixels.
            margin (:obj:`int`): Distance between cells in pixels.
            cells_in_row (:obj:`int`): Count of the cells in row.
        """

        self.cell_height = height
        self.cell_width = width
        self.margin = margin
        self.cells_in_row = self.cells_in_column = cells_in_row

        self._default_color = (0, 0, 0)
        self._grid = self._grid_init()

    def draw(self, screen, pygame):
        """
        Draw the grid on the screen using pygame object.

        Args:
            :obj:`screen`: specified the screen where a snake will be drawn.
            :obj:`pygame`: used to call ``draw`` method.
        """

        for row in range(self.cells_in_row):
            for column in range(self.cells_in_column):
                pygame.draw.rect(screen,
                                 self._grid[row][column],
                                 [(self.margin + self.cell_width) * row + self.margin,
                                  (self.margin + self.cell_height) * column + self.margin,
                                  self.cell_width,
                                  self.cell_height])

    def screen_size(self):
        """
        Calculates the screen coordinates according to established grid params.

        Returns:
             :obj:`list`: width and height of the screen in pixels.
        """

        width = self.margin + self.cells_in_row * (self.cell_width + self.margin)
        height = self.margin + self.cells_in_row * (self.cell_height + self.margin)

        return [width, height]

    def clear(self):
        """Set all cells in the grid to default color."""

        for row in self._grid:
            for cell in row:
                cell = self.default_color

    def to_grid_coordinates(self, screen_x, screen_y):
        """
        Convert screen coordinates to grid coordinates.

        Raises:
            OutOfCellsBoundError: if screen coordinates are negative or between cells.

        Returns:
             :obj:`tuple`: converted cell coordinates.
        """

        x_remainder = screen_x % (self.cell_width + self.margin)
        y_remainder = screen_y % (self.cell_width + self.margin)

        if x_remainder < self.margin or y_remainder < self.margin:
            raise OutOfCellsBoundError("Passing coordinates are between cells.")
        if screen_x < 0 or screen_y < 0:
            raise OutOfCellsBoundError("Passing coordinates are negative.")

        cell_x = int(screen_x / (self.cell_width + self.margin))
        cell_y = int(screen_y / (self.cell_width + self.margin))

        return cell_x, cell_y

    def set_color_of_cell(self, color, x, y):
        """
        Set the color of the cell with coordinates x and y.

        Params:
            :obj:`tuple` color: the color in RGB format
            :obj:`int` x: x coordinate of setting cell
            :obj:`int` y: y coordinate of setting cell
        """

        self._grid[x][y] = color

    def _grid_init(self):
        grid = [[self.default_color for x in range(self.cells_in_row)] for y in range(self.cells_in_row)]

        return grid

    def is_coordinates_out_of_grid(self, cell_x, cell_y):
        """
         Verify if the coordinates are out of grid.

        Args:
            :obj:`int` cell_x: x coordinate of the cell
            :obj:`int` cell_y: y coordinate of the cell

        Returns:
             True if coordinates are out of grid else False.
        """

        return cell_x < 0 \
            or cell_y < 0 \
            or cell_x >= self.cells_in_row \
            or cell_y >= self.cells_in_column

    @property
    def grid(self):
        """:obj:`list` of :obj:`list`: grid"""
        return self._grid.copy()

    @property
    def default_color(self):
        """:obj:`tuple`: color in RGB format"""

        return self._default_color

    @default_color.setter
    def default_color(self, red, green, blue):

        self.default_color = (red, green, blue)

# http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
