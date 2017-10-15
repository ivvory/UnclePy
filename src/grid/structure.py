class GridStructure:
    def __init__(self, grid, cells, color):
        self.grid = grid
        self.grid.structures += [self]
        self.color = color

        self.cells = []
        self + cells

    def __add__(self, cells: list):
        self.conquer(cells)

    def __sub__(self, cells: list):
        self.lose(cells)

    def conquer(self, cells: list):
        """

        Args:

        """
        for c in cells:
            c.occupy(self)

    def lose(self, cells: list):
        """

        Args:

        """

        self.grid.main_structure.conquer(cells)
