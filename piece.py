'''
Module for different pieces. Will serve as generator.
The different O, I, T, L, J, S and Z pieces will be created here.
'''

from enum import Enum
from copy import deepcopy

class PieceState(Enum):
    '''Represents the current state of a piece in a given moment'''
    CAN_PLACE = 0
    BLOCKED = 1
    OFFSCREEN = 2

class PieceType(Enum):
    '''Represents the type of a piece'''
    O = 1
    I = 2
    T = 3
    L = 4
    J = 5
    S = 6
    Z = 7

class Piece:
    '''Base class for different pieces.'''
    SHAPES = (
        [
            [1, 1],
            [1, 1],
        ],
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 1, 1],
            [1, 1, 0],
            [0, 0, 0],
        ],
        [
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0],
        ],
    )

    COLORS = [
        (0, 0, 0),
        (255, 255, 0),
        (0, 255, 255),
        (220, 0, 220),
        (255, 128, 0),
        (0, 0, 255),
        (0, 255, 0),
        (255, 0, 0),
    ]

    def generate_piece(piece_index=1):
        '''Class method. Generates a piece from a given index.'''
        return Piece(piece_index)

    def __init__(self, piece_type=PieceType.O.value):
        '''Constructor method'''
        self.piece_type = piece_type
        self.shape = deepcopy(Piece.SHAPES[piece_type - 1])
        self.length = len(self.shape)
        self.pos_x = 5 - self.length // 2
        self.pos_y = 2

    def __getitem__(self, index):
        '''Returns the row in the shape of the piece'''
        return self.shape[index]

    def can_place(self, grid, piece=[], dx=0, dy=0):
        '''Checks if a piece can be placed at it's given position'''
        x, y = (self.pos_x, self.pos_y)

        for i in range(y, y + self.length):
            for j in range(x, x + self.length):
                if piece[i - y][j - x] != 0:
                    if not grid.is_inside_grid(i + dy, j + dx):
                        return PieceState.OFFSCREEN

                    if grid[i + dy][j + dx] != 0:
                        return PieceState.BLOCKED

        return PieceState.CAN_PLACE

    def rotate(self, grid):
        '''Rotate method'''
        rotated_piece = [[0 for i in range(self.length)] for j in range(self.length)]

        for i in range(self.length):
            for j in range(self.length):
                rotated_piece[i][j] = self.shape[self.length - 1 - j][i]

        p_state = self.can_place(grid, rotated_piece)

        if p_state == PieceState.CAN_PLACE:
            self.shape = deepcopy(rotated_piece)

        elif p_state == PieceState.OFFSCREEN:
            if self.pos_x < 0:
                self.pos_x = 0
            # elif self.pos_x > grid.width:
            else:
                self.pos_x = grid.width - self.length
            self.shape = deepcopy(rotated_piece)

    def dropdown(self, grid):
        '''Dropdown a piece'''

        for i in range(1, grid.height - self.pos_y):
            if not self.can_place(grid, self.shape, dy=i) == PieceState.CAN_PLACE:
                return i - 1

        return 0

