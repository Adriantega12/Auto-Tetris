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
    shapes = (
        [
            [1, 1],
            [1, 1],
        ],
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1],
        ],
        [
            [0, 0, 0],
            [0, 0, 1],
            [1, 1, 1],
        ],
        [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 1],
        ],
        [
            [0, 0, 0],
            [0, 1, 1],
            [1, 1, 0],
        ],
        [
            [0, 0, 0],
            [1, 1, 0],
            [0, 1, 1],
        ],
    )

    def generate_piece(piece_index=1):
        '''Class method. Generates a piece from a given index.'''
        return Piece(piece_index)

    def __init__(self, piece_type=PieceType.O.value):
        '''Constructor method'''
        self.piece_type = piece_type
        self.shape = deepcopy(Piece.shapes[piece_type - 1])
        self.pos_x = 0
        self.pos_y = 2
        self.length = len(self.shape)

    def __getitem__(self, index):
        '''Returns the row in the shape of the piece'''
        return self.shape[index]

    def rotate(self):
        '''Rotate method'''
        rotatedPiece = [[0 for i in range(self.length)] for j in range(self.length)]

        '''
        [[0 0 0]     [[1 0 0]
         [0 1 0]  =>  [1 1 0]
         [1 1 1]]     [1 0 0]]
        '''

        for i in range(self.length):
            for j in range(self.length):
                rotatedPiece[i][j] = self.shape[self.length - 1 - j][i]

        self.shape = deepcopy(rotatedPiece)
