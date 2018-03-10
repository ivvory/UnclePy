class GridStructure:
    def __init__(self, grid, cells, color):
        self.grid = grid
        self.color = color

        self.cells = []
        self + cells

    def __add__(self, cells: list):
        self.conquer(cells)

    def __sub__(self, cells: list):
        self.lose(cells)

    def conquer(self, cells: list):
        """Occupies passed `cells` by itself.

        Args:
            cells: occupying by snake
        """
        for c in cells:
            c.occupy(self)

    def lose(self, cells: list):
        """Give back `cells` to the grid.

        Params:
            cells: giving back
        """

        self.grid.main_structure.conquer(cells)
