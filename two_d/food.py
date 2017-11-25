# from two_d.grid.grid import BasicGrid
from two_d.grid.structure import GridStructure


class Food(GridStructure):
    """
        Manage a food on the grid.
    """

    def __init__(self, grid, cell, color: tuple, value: int):
        super().__init__(grid, [cell], color)

        self.value = value
