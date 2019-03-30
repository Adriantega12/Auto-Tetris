'''Grid class module. Basically the game board.'''

class Grid:
    '''Grid class object to represent grid.'''

    def __init__(self, grid_width=10, grid_height=22):
        '''Init function.'''
        self.grid = [[0 for i in range(grid_width)] for j in range(grid_height)]

    def __getitem__(self, index):
        '''Access to grid using brackets as if it was just a matrix.'''
        return self.grid[index]

    def setPiece(self, piece):
        '''This method will set the piece in the position where piece is'''
        print(piece.length())

        for i in range(piece.length()): # Y
            for j in range(piece.length()): # X
                self.grid[piece.pos_y + j][piece.pos_x + i] = piece.shape[j][i]

    def print(self):
        '''Print grid to console.'''
        for row in self.grid:
            print(row)
