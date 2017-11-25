from two_d.grid.structure import GridStructure


class GridCell:
    def __init__(self, coordinates: tuple, owner: GridStructure = None):
        self.coordinates = coordinates
        self.owner = owner
        self.changed = False

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    @property
    def color(self):
        return self.owner.color

    def occupy(self, new_owner):
        if self.owner:
            self.owner.cells.remove(self)

        self.owner = new_owner
        self.owner.cells.append(self)

        self.changed = True
