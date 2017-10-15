from src.grid.structure import GridStructure


class GridCell:
    def __init__(self, coordinates: tuple, owner: GridStructure = None):
        self.coordinates = coordinates
        self.owner = owner

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    @property
    def color(self):
        return self.owner.color

    def occupy(self, new_owner):
        self.owner - [self]
        self.owner = new_owner
