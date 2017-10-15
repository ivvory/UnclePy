class GridStructure:
    def __init__(self, grid, cells, color):
        self.grid = grid
        self.grid.structures += [self]
        self.color = color

        self.cells = []
        self + cells

    def __add__(self, cells: list):
        self.conquer(list(c.coordinates for c in cells))

    def __sub__(self, cells: list):
        self.lose(list(c.coordinates for c in cells))

    def conquer(self, coordinates: list) -> list:
        """

        Args:

        """
        conquered_cells = [self.grid.get_cell(*coord) for coord in coordinates]
        for c in conquered_cells:
            c.owner = self

        self.cells += conquered_cells

        return conquered_cells

    def lose(self, coordinates: list):
        """

        Args:

        """

        self.grid.main_structure.conquer(coordinates)
