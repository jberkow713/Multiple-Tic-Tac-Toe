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

Used_Squares = []
Players = []
GAME_OVER = False
Winning_Lines = {}

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

class Comp_Player:
    def __init__(self, Board, color, shape, to_win):
        self.Board = Board
        self.color = color
        self.shape = shape
        self.keys = self.key_amounts()
        self.to_win = to_win
        self.Circles = []
        self.Xs = []
        self.add_to_list()
        # Checking to see if Winning_Lines Exist, 
        # They will be created by first computer player, 
        # and used by the others
        if len(Winning_Lines.keys())==0:
            self.create_winning_lines()

    def create_winning_lines(self):

        # Create All possible Winning Lines for the Board, 
        # Store in the Global Dictionary
        square = 0
        Matrix = []
        for _ in range(self.Board.dimensions):
            L = []
            for _ in range(self.Board.dimensions):
                L.append(square)
                square+=1
            Matrix.append(L)

        winning_lines = []
        # Row Winning Lines
        rows = len(Matrix)
        row_index = 0    
        while rows >0:
            count = 0
            curr_index = 0
            index = 0
            row = Matrix[row_index]
            row_winning_lines = []
            while index < self.Board.dimensions:
                curr = row[index]
                row_winning_lines.append(curr)
                count +=1
                index +=1
                if count ==self.to_win:
                    winning_lines.append(row_winning_lines)
                    row_winning_lines = []
                    count = 0
                    curr_index +=1
                    index = curr_index    
            row_index +=1
            rows -=1
        # Column Winning Lines
        cols = len(Matrix)
        col_index = 0

        while cols >0:
            count = 0
            curr_index = 0
            row_index = 0
            col_winning_lines = []
            while row_index < self.Board.dimensions:
                Curr = Matrix[row_index][col_index]
                col_winning_lines.append(Curr)
                count +=1
                row_index +=1
                if count == self.to_win:
                    winning_lines.append(col_winning_lines)
                    col_winning_lines = []
                    count = 0
                    curr_index +=1
                    row_index = curr_index
            col_index +=1
            cols -=1
        # Diagonal Down Winning Lines
        rows = len(Matrix)-self.to_win+1
        row = 0
        
        while rows >0:
            count = 0
            curr_index = 0
            row_index = row
            col_index = 0
            diag_winning_lines = []
            while col_index < self.Board.dimensions:
                Curr = Matrix[row_index][col_index]
                diag_winning_lines.append(Curr)
                count +=1
                row_index +=1
                col_index +=1
                if count == self.to_win:
                    winning_lines.append(diag_winning_lines)
                    diag_winning_lines = []
                    count = 0
                    row_index = row
                    curr_index +=1
                    col_index = curr_index
            row +=1
            rows -=1

        rows = len(Matrix)-self.to_win+1
        row = self.Board.dimensions-1
        while rows >0:
            count = 0
            curr_index = 0
            row_index = row
            col_index = 0
            diag_winning_lines = []
            
            while col_index < self.Board.dimensions:
                Curr = Matrix[row_index][col_index]
                diag_winning_lines.append(Curr)
                count +=1
                row_index -=1
                col_index +=1
                if count == self.to_win:
                    winning_lines.append(diag_winning_lines)
                    diag_winning_lines = []
                    count = 0
                    row_index = row
                    curr_index +=1
                    col_index = curr_index
            row -=1
            rows -=1

        vals = [self.to_win for x in range(len(winning_lines))]
        winning_lines = [tuple(x) for x in winning_lines]
        global Winning_Lines
        Winning_Lines = dict(zip(winning_lines,vals))
        return        

    def add_to_list(self):
        Players.append(self)

    def key_amounts(self):        
        return (self.Board.dimensions**2)-1

    def add_circle(self, index):
        self.Circles.append(index)
    
    def add_X(self, index):
        self.Xs.append(index)
    
    def draw_circle(self):
        for pos in self.Circles:
            Position = self.Board.Circle_Positions[pos]
            pygame.draw.circle(self.Board.screen.view, self.color, Position, self.Board.square_size, 3)
    
    def draw_X(self):        
        for pos in self.Xs:
            Positions = self.Board.Square_Positions
            L1 = Line(self.Board.screen, Positions[pos][0], Positions[pos][1], self.color)
            L2 = Line(self.Board.screen, Positions[pos][2], Positions[pos][3], self.color)
            L1.draw(5)
            L2.draw(5)

    def add_to_Global(self, index):
        Used_Squares.append(index)
        return
        
    def Action(self):
        if len(Used_Squares)== self.Board.dimensions**2:
            global GAME_OVER
            GAME_OVER = True
            return            

        Exit =False
        while Exit==False:
            #Logic function built in here, to choose from keys
            #For now, it is random 
            Choice = random.randint(0,self.keys)
            
            if self.shape == 'O':
                if Choice not in self.Circles and Choice not in Used_Squares:
                    self.add_circle(Choice)
                    self.add_to_Global(Choice)
                    Exit = True
            if self.shape == 'X':
                if Choice not in self.Xs and Choice not in Used_Squares:
                    self.add_X(Choice)
                    self.add_to_Global(Choice)
                    Exit = True
                           
        if self.shape == 'O':            
            self.draw_circle()

        elif self.shape =='X':
                        
            self.draw_X()
            
        return

pygame.init()
clock = pygame.time.Clock()
B = Board(9,50,1000, 1000, LINE_COLOR, BOARD_COLOR)

C = Comp_Player(B, BLUE,'X',5)
C2 = Comp_Player(B, RED, 'O',5)
C3 = Comp_Player(B, GREEN, 'O',5)
C4 = Comp_Player(B, PURPLE, 'X',5)

print(Winning_Lines)

# Need to keep track of each of the spots being drawn for each player, in their list,
# Then in each loop iteration, need to draw all the spots in the players list by that player


# while True:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
    
#     B.draw_board()
    
#     for Player in Players:
#         Player.Action()         

#     pygame.display.set_caption("Multiplayer_Tic_Tac_Toe")
#     pygame.display.flip()