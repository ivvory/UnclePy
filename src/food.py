from src.grid.grid import BasicGrid
from src.grid.structure import GridStructure


class Food(GridStructure):
    """
        Manage a food on the grid.
    """

    def __init__(self, grid: BasicGrid, coordinates: tuple, color: tuple, value: int):
        super().__init__(grid, [grid.get_cell(*coordinates)], color)

        self.value = value
