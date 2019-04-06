'''Grid class module. Basically the game board.'''

class Grid:
    '''Grid class object to represent grid.'''

    def __init__(self, grid_width=10, grid_height=22):
        '''Init function.'''
        self.width = grid_width
        self.height = grid_height
        self.grid = [[0 for i in range(grid_width)] for j in range(grid_height)]

    def __getitem__(self, index):
        '''Access to grid using brackets as if it was just a matrix.'''
        return self.grid[index]

    def is_inside_grid(self, i, j):
        '''Tests if a given position is inside the grid'''
        return 0 <= i < self.height and 0 <= j < self.width

    def set_piece(self, piece):
        '''This method will set the piece in the position where piece is'''
        for i in range(piece.length): # Y
            for j in range(piece.length): # X
                if piece[i][j] != 0 and self.is_inside_grid(
                        piece.pos_y + i,
                        piece.pos_x + j,
                    ):
                    self.grid[piece.pos_y + i][piece.pos_x + j] = piece.piece_type * piece.shape[i][j]

    def can_place(self, piece, dx=0, dy=0):
        '''Checks if a piece can be placed at it's given position'''
        x, y = (piece.pos_x, piece.pos_y)

        for i in range(y, y + piece.length):
            for j in range(x, x + piece.length):
                if piece[i - y][j - x] != 0:
                    if not self.is_inside_grid(i + dy, j + dx):
                        print(i, j)
                        print('Outside grid')
                        return False

                    if self.grid[i + dy][j + dx] != 0:
                        print('Is 1')
                        return False

        return True

    def print(self):
        '''Print grid to console.'''
        for i in range(2, 22):
            print(self.grid[i])
            # print(i, self.grid[i])
