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

    def __init__(self, piece_type=PieceType.O):
        '''Constructor method'''
        self._piece_type = piece_type
        self.shape = deepcopy(Piece.shapes[piece_type.value - 1])
        self.pos_x = 0
        self.pos_y = 0

    def length(self):
        '''
        Returns the length of the piece.
        Since all pieces are contained in square matrixes, will just return the length of shape.
        '''
        return len(self.shape)

    def rotate(self):
        '''Rotate method'''