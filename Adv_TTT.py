import math
import random 
from copy import deepcopy
import numpy as np
import pygame
import sys

#Dimensions
WIDTH = 1500 
HEIGHT = 1000 
FPS = 60
# Colors
GROUND_COLOR = (255, 222, 179)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)
LINE_COLOR = BLUE
BOARD_COLOR = WHITE 

class Screen:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.view = self.build_screen()
        self.fill_screen()
            
    def build_screen(self):

        VIEW = pygame.display.set_mode((self.width, self.height))
        return VIEW
    
    def fill_screen(self):
        self.view.fill(self.color)

class Line:
    def __init__(self, Screen,starting, ending, color):
        # starting and ending are tuples, x/y coordinates
        self.Screen = Screen
        self.starting = starting
        self.ending = ending
        self.color = color       
        
    def draw(self):
        pygame.draw.line(self.Screen.view, self.color, self.starting, self.ending)      

class Board:
    def __init__(self, dimensions, Buffer, Screen_Width, Screen_Height, line_color, screen_color):
        self.dimensions = dimensions
        self.Buffer = Buffer
        self.Width = Screen_Width
        self.Height = Screen_Height
        self.line_color = line_color
        self.screen_color = screen_color
        self.screen = self.build_screen()
        self.lines = []
        self.create_lines()
        self.draw_board()

    def build_screen(self):
        screen = Screen(self.Width, self.Height, self.screen_color)
        return screen

    def create_lines(self):
        Buff = self.Buffer
        screen = self.screen
        self.lines.append(Line(screen,(Buff,Buff), (self.Width-Buff,Buff), self.line_color))
        self.lines.append(Line(screen,(Buff,self.Height-Buff), (self.Width-Buff,self.Height-Buff), self.line_color))
        self.lines.append(Line(screen,(Buff,Buff), (Buff,self.Height-Buff), self.line_color))
        self.lines.append(Line(screen,(self.Width-Buff,Buff), (self.Width-Buff,self.Height-Buff), self.line_color))

        X_Gap = (self.Width - 2*Buff) / self.dimensions
        Y_Gap = (self.Height -2*Buff) / self.dimensions

        for i in range(self.dimensions):
            Vert_L = Line(screen, (Buff + i*X_Gap,Buff), (Buff + i*X_Gap, self.Height-Buff), self.line_color)
            self.lines.append(Vert_L)
            Hor_L = Line(screen, (Buff ,Buff+i*Y_Gap), (self.Width-Buff, Buff+i*Y_Gap), self.line_color)
            self.lines.append(Hor_L)

    def draw_board(self):
        for x in self.lines:
            x.draw()         

pygame.init()
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    B = Board(9,50,WIDTH, HEIGHT, LINE_COLOR, BOARD_COLOR)
    
    pygame.display.set_caption("Multiplayer_Tic_Tac_Toe")
    pygame.display.flip()