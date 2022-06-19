import math
import random 
from copy import deepcopy
import numpy as np
import pygame
import sys

#Dimensions
BOARD_WIDTH = 1500 
BOARD_HEIGHT = 1000 
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
        # The View is the actual Pygame Surface
        self.view = self.build_screen()
        self.fill_screen()
            
    def build_screen(self):

        return pygame.display.set_mode((self.width, self.height))        
    
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
        self.screen = self.return_screen()
        self.lines = []
        self.square_size = None
        self.Positions = {}
        self.create_lines()
        self.draw_board()
        

    def return_screen(self):

        return Screen(self.Width, self.Height, self.screen_color)
        
    def create_lines(self):
        Buff = self.Buffer
        screen = self.screen
        
        X_Gap = (self.Width - 2*Buff) / self.dimensions
        Y_Gap = (self.Height -2*Buff) / self.dimensions
        self.square_size = X_Gap/2

        for i in range(self.dimensions+1):
            Vert_L = Line(screen, (Buff + i*X_Gap,Buff), (Buff + i*X_Gap, self.Height-Buff), self.line_color)
            self.lines.append(Vert_L)
            Hor_L = Line(screen, (Buff ,Buff+i*Y_Gap), (self.Width-Buff, Buff+i*Y_Gap), self.line_color)
            self.lines.append(Hor_L)
        
        count = 0
        for i in range(self.dimensions):
            y_val = Buff + i*Y_Gap +.5*Y_Gap
            

            for j in range(self.dimensions):
                x_val = Buff+j*X_Gap + .5*X_Gap                
                self.Positions[count]=(x_val,y_val)
                count +=1
        

    def draw_board(self):
        for x in self.lines:
            x.draw()         

pygame.init()
clock = pygame.time.Clock()
B = Board(13,50,1000, 1000, LINE_COLOR, BOARD_COLOR)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    B
    pygame.draw.circle(B.screen.view, RED, B.Positions[(B.dimensions**2+1)/2 -1], B.square_size, 5)
    
    pygame.display.set_caption("Multiplayer_Tic_Tac_Toe")
    pygame.display.flip()