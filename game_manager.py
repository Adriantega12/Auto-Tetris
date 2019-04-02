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

        self.display = pygame.display.set_mode((500, 300), pygame.SRCALPHA, 32)

        self.frames = 0
        self.speed = 30

        self.grid = Grid()
        self.gGrid = Grid()
        self.piece = Piece()

    def handle_events(self):
        '''Handle all events in the event queue'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Bye bye')
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.piece.pos_x += -1
                    print('Left')
                elif event.key == pygame.K_d:
                    self.piece.pos_x += 1
                    print('Right')
                print('Bitch')

    def update(self):
        '''Update part from the loop. All logic should be managed from here.'''
        if self.frames % self.speed == 0:
            self.piece.pos_y += 1

        self.gGrid.grid = deepcopy(self.grid.grid)
        self.gGrid.set_piece(self.piece)

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

            self.handle_events()

            self.update()
            self.print()
