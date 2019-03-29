
GRID_HEIGHT = 22
GRID_WIDTH = 10

class Grid:
  '''Class that represents the game board where pieces will fall and stack up'''

  GRID_HEIGHT = 22
  GRID_WIDTH = 10

  def __init__(self):
    '''Init function'''
    self._grid = [ [ 0 for i in range(GRID_WIDTH) ] for j in range(GRID_HEIGHT) ]

  def __getitem__(self, index):
    '''Indexing of grid to get grid rows or even individual cells using double indexing'''
    return self._grid[index]

  def Print(self):
    for row in self._grid:
      print(row)

g = Grid()
