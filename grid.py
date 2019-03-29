"""Grid class module. Basically the game board."""


class Grid:
    """Grid class object to represent grid."""

    GRID_HEIGHT = 22
    GRID_WIDTH = 10

    def __init__(self):
        """Init function."""
        self._grid = [[0 for i in range(Grid.GRID_WIDTH)] for j in range(Grid.GRID_HEIGHT)]

    def __getitem__(self, index):
        """Access to grid using brackets as if it was just a matrix."""
        return self._grid[index]

    def print(self):
        """Print grid to console."""
        for row in self._grid:
            print(row)
