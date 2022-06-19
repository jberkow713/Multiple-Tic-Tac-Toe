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
        
    def draw(self, width=None):
        if width == None:
            pygame.draw.line(self.Screen.view, self.color, self.starting, self.ending)      
        else:
            pygame.draw.line(self.Screen.view, self.color, self.starting, self.ending, width)   

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
        # Circle Positions represent the center of each square
        self.Circle_Positions = {}
        self.Square_Positions = {}  
        self.create_lines()                   

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
        #Circle Creation 
        count = 0
        for i in range(self.dimensions):
            y_val = Buff + i*Y_Gap +.5*Y_Gap            

            for j in range(self.dimensions):
                x_val = Buff+j*X_Gap + .5*X_Gap                
                self.Circle_Positions[count]=(x_val,y_val)
                count +=1        
        #X_Creation
        count = 0
        for i in range(self.dimensions):
            y_val_1 = Buff + i*Y_Gap
            y_val_2 = Buff + (i+1)*Y_Gap
                       
            for j in range(self.dimensions):
                x_val_1 = Buff + j*X_Gap
                x_val_2 = Buff + (j+1)*X_Gap
                self.Square_Positions[count]=[(x_val_1,y_val_1),(x_val_2,y_val_2),(x_val_1,y_val_2),(x_val_2,y_val_1) ]  
                count +=1
       
    def draw_board(self):
        for x in self.lines:
            x.draw()
                     
# Board.Positions[(B.dimensions**2+1)/2 -1]
class Comp_Player:
    def __init__(self, Board, color):
        self.Board = Board
        self.color = color
        self.Circles = []
        self.Xs = []
    def add_circle(self, index):
        if index not in self.Circles:
            self.Circles.append(index)
    def add_X(self, index):
        if index not in self.Xs:
            self.Xs.append(index)
    def draw_circle(self):
        for pos in self.Circles:
            Position = self.Board.Circle_Positions[pos]
            pygame.draw.circle(self.Board.screen.view, self.color, Position, self.Board.square_size, 3)
    def draw_X(self):
        # [(518.0, 806.0), (554.0, 842.0), (518.0, 842.0), (554.0, 806.0)]
        for pos in self.Xs:

            Positions = self.Board.Square_Positions
            L1 = Line(self.Board.screen, Positions[pos][0], Positions[pos][1], self.color)
            L2 = Line(self.Board.screen, Positions[pos][2], Positions[pos][3], self.color)
            L1.draw(5)
            L2.draw(5)
   
pygame.init()
clock = pygame.time.Clock()
B = Board(25,50,1000, 1000, LINE_COLOR, BOARD_COLOR)
C = Comp_Player(B, BLUE)
C2 = Comp_Player(B,RED)
C3 = Comp_Player(B, GREEN)

# Need to keep track of each of the spots being drawn for each player, in their list,
# Then in each loop iteration, need to draw all the spots in the players list by that player
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    B.draw_board()
    C.add_circle(25)
    C.add_circle(30)
    C.draw_circle()   
    C2.add_X(35)
    C2.draw_X()
    C3.add_circle(50)
    C3.draw_circle()

    pygame.display.set_caption("Multiplayer_Tic_Tac_Toe")
    pygame.display.flip()