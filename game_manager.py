'''
Game manager module.
From here the game loop will run. All the other elements of the game will be made class members.
'''

from os import system
from copy import deepcopy
from random import randint
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
        self.piece = Piece.generate_piece(randint(1, 7))

    def handle_events(self):
        '''Handle all events in the event queue'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Bye bye')
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.piece.rotate()
                else:
                    d = int(event.key == pygame.K_d) - int(event.key == pygame.K_a)
                    if self.piece.can_place(
                            #piece=self.piece,
                            grid=self.grid,
                            dx=d,
                        ):
                        self.piece.pos_x += d

    def update(self):
        '''Update part from the loop. All logic should be managed from here.'''
        if self.frames % self.speed == 0:
            if self.piece.can_place(
                    #piece=self.piece,
                    grid=self.grid,
                    dy=1,
                ):
                self.piece.pos_y += 1
            else:
                # Place piece
                self.grid.set_piece(self.piece)
                self.piece = Piece.generate_piece(randint(1, 7))

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
        print('Piece type: ', self.piece.piece_type)

    def loop(self):
        '''Game loop'''
        clock = pygame.time.Clock()

        while True:
            clock.tick(30)
            self.frames += 1

            self.handle_events()

            self.update()
            self.print()
