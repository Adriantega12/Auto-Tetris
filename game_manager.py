'''
Game manager module.
From here the game loop will run. All the other elements of the game will be made class members.
'''

from os import system
import sys
from copy import deepcopy
from random import randint
from joblib import load
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
import pygame
from grid import Grid
from piece import Piece, PieceState
from data_gen import DataGenerator

class GameManager:
    '''Game manager class. Manages the main game loop and will manage other things as events.'''

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((600, 660), pygame.SRCALPHA, 32)

        # Game level (Probably should modify this)
        self.frames = 0
        self.speed = 15

        # Game essentials
        self.grid = Grid()
        self.gGrid = Grid()
        self.piece = Piece.generate_piece(randint(1, 7))

        # Data generation for the neural network
        self.data_gen = DataGenerator()

        # Arg flags
        self.is_human = True
        self.debug_mode = False
        self.model = None
        self.flag_setup()

    def flag_setup(self):
        '''Setup function for whatever is needed'''
        arguments = sys.argv[1:]

        if '-ai' in arguments:
            print('AI is working')
            self.is_human = False
            ai_file = arguments[arguments.index('-ai') + 1]
            self.model = load(ai_file)

        if '-debug' in arguments:
            self.debug_mode = True

        if '-o' in arguments:
            pass

    def handle_events(self):
        '''Handle all events in the event queue'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Bye bye')
                exit()

            if self.is_human:
                self.handle_human_input(event)

        if not self.is_human:
            row = []
            for i in range(self.gGrid.height):
                for j in range(self.gGrid.width):
                    row.append(int(self.gGrid[i][j] > 0))
            row.append(self.piece.piece_type)
            reshaped_row = np.asarray(row).reshape(1, -1)
            move = self.model.predict(reshaped_row)[0]

            if move == 1:
                self.rotate()
            elif move == 2:
                self.dropdown()
            elif move == 3:
                self.move_right()
            elif move == 4:
                self.move_left()


    def handle_human_input(self, event):
        '''Handle human input if control is given'''
        if event.type == pygame.KEYDOWN:
            # Rotation
            if event.key == pygame.K_r:
                self.rotate()
                self.data_gen.write_grid(self.gGrid, self.piece.piece_type, 1)

            # Drop down
            elif event.key == pygame.K_s:
                self.dropdown()
                self.data_gen.write_grid(self.gGrid, self.piece.piece_type, 2)

            elif event.key == pygame.K_d:
                self.move_right()
                self.data_gen.write_grid(self.gGrid, self.piece.piece_type, 3)

            elif event.key == pygame.K_a:
                self.move_left()
                self.data_gen.write_grid(self.gGrid, self.piece.piece_type, 4)

    def rotate(self):
        self.piece.rotate(self.grid)

    def dropdown(self):
        self.piece.pos_y += self.piece.dropdown(self.grid)

    def move_right(self):
        if self.piece.can_place(
                piece=self.piece.shape,
                grid=self.grid,
                dx=1,
            ) == PieceState.CAN_PLACE:
            self.piece.pos_x += 1

    def move_left(self):
        if self.piece.can_place(
                piece=self.piece.shape,
                grid=self.grid,
                dx=-1,
            ) == PieceState.CAN_PLACE:
            self.piece.pos_x += -1

    def update(self):
        '''Update part from the loop. All logic should be managed from here.'''
        if self.frames % self.speed == 0:
            if self.piece.can_place(
                    #piece=self.piece,
                    piece=self.piece.shape,
                    grid=self.grid,
                    dy=1,
                ) == PieceState.CAN_PLACE:
                self.piece.pos_y += 1
                if self.is_human:
                    self.data_gen.write_grid(self.gGrid, self.piece.piece_type, 0)
            else:
                # Place piece
                self.grid.set_piece(self.piece)
                self.grid.check_completition()
                self.piece = Piece.generate_piece(randint(1, 7))

        self.gGrid.grid = deepcopy(self.grid.grid)
        self.gGrid.set_piece(self.piece)

    def render(self):
        '''Render method of the game loop. Here everything will be rendered.'''
        self.display.fill((100, 100, 100))
        self.gGrid.render(self.display, x=10, y=20)
        pygame.display.update()

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

        # self.setup()

        while True:
            clock.tick(30)
            self.frames += 1

            self.handle_events()

            self.update()
            self.render()

            if self.debug_mode:
                self.print()
