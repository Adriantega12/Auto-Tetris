'''Grid class module. Basically the game board.'''

from pygame import draw, image
from piece import Piece

class Grid:
    '''Grid class object to represent grid.'''

    def __init__(self, grid_width=10, grid_height=22, cell_size=29):
        '''Init function.'''
        self.width = grid_width
        self.height = grid_height
        self.grid = [[0 for i in range(grid_width)] for j in range(grid_height)]
        self.cell_size = cell_size

        self.tile = image.load('./assets/tile2.png').convert_alpha()

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

    def check_completition(self):
        '''Method to remove a row on completition and let the rest of the stack fall'''
        for row in self.grid:
            complete = True
            for cell in row:
                if cell == 0:
                    complete = False
            if complete:
                self.grid.remove(row)
                self.grid.insert(0, [0 for i in range(self.width)])

    def render(self, display, x=8, y=8):
        '''Render method of the grid, should render all the grid'''

        # Background
        draw.rect(
            display,
            (66, 134, 244),
            (x, y, self.cell_size * self.width, self.cell_size * (self.height - 2)),
            )
        # Grid
        GRID_COLOR = (55, 123, 222)
        for i in range(self.height - 2):
            draw.line(
                display,
                GRID_COLOR,
                (x, y + i * self.cell_size),
                (x + self.cell_size * self.width, y + i * self.cell_size),
                )
        for i in range(self.width):
            draw.line(
                display,
                GRID_COLOR,
                (x + i * self.cell_size, y),
                (x + i * self.cell_size, y + self.cell_size * (self.height - 2)),
                )
        # Draw all cells
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] != 0:
                    # Draw colored cell
                    draw.rect(
                        display,
                        Piece.COLORS[self.grid[i][j]],
                        (
                            x + j * self.cell_size,
                            y + (i - 2) * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                            ),
                        )
                    # Draw shade
                    display.blit(
                        self.tile,
                        (
                            x + j * self.cell_size,
                            y + (i - 2) * self.cell_size,
                            ),
                        )

    def print(self):
        '''Print grid to console.'''
        for i in range(self.height):
            print(self.grid[i])
