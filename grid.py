"""Grid class module. Basically the game board."""


class Grid:
    """Grid class object to represent grid."""

    def __init__(self, grid_width=10, grid_height=22):
        """Init function."""
        self._grid = [[0 for i in range(grid_width)] for j in range(grid_height)]

    def __getitem__(self, index):
        """Access to grid using brackets as if it was just a matrix."""
        return self._grid[index]

    def print(self):
        """Print grid to console."""
        for row in self._grid:
            print(row)
