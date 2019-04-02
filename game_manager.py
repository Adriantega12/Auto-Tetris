'''
Game manager module.
From here the game loop will run. All the other elements of the game will be made class members.
'''

from os import system
from copy import deepcopy
import pygame
from grid import Grid
from piece import Piece

class GameManager:
    '''Game manager class. Manages the main game loop and will manage other things as events.'''

    def __init__(self):
        pygame.init()

        self.frames = 0
        self.speed = 30

        self.grid = Grid()
        self.gGrid = Grid()
        self.piece = Piece()

    def update(self):
        '''Update part from the loop. All logic should be managed from here.'''
        if self.frames % self.speed == 0:
            self.piece.pos_y += 1
            self.gGrid.grid = deepcopy(self.grid.grid)
            self.gGrid.setPiece(self.piece)



    def print(self):
        '''
        Print part from the loop. The grid will be printed from here.
        If there is enough time, print will be eventually be made into a render function
        for functional graphics.
        '''
        system('clear')
        self.gGrid.print()

    def loop(self):
        '''Game loop'''
        clock = pygame.time.Clock()

        while True:
            clock.tick(30)
            self.frames += 1

            self.update()
            self.print()
