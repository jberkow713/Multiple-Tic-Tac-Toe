import math
import random 
from copy import deepcopy
import numpy as np
import pygame
import sys

WIDTH = 1500 #1800
HEIGHT = 1000 #1400
FPS = 60
# Colors
GROUND_COLOR = (255, 222, 179)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)

class Screen:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.view = self.build_screen()
            
    def build_screen(self):

        VIEW = pygame.display.set_mode((self.width, self.height))
        return VIEW
    
    def fill_screen(self):
        self.view.fill(self.color)

        

pygame.init()
clock = pygame.time.Clock()
screen = Screen(WIDTH, HEIGHT, WHITE)
screen.fill_screen() 


class Line:
    def __init__(self, starting, ending, color):
        # starting and ending are tuples, x/y coordinates
        self.starting = starting
        self.ending = ending
        self.color = color
        
        
    def draw(self):
        pygame.draw.line(screen.view, self.color, self.starting, self.ending)      

class Board:
    def __init__(self, dimensions, Buffer, Screen_Width, Screen_Height):
        self.dimensions = dimensions
        self.Buffer = Buffer
        self.Width = Screen_Width
        self.Height = Screen_Height

    def draw(self):

        pass 
            

L = Line((50,50), (1450,50), BLUE)
L2 = Line((50,screen.height-50), (1450,screen.height-50), BLUE)  

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    L.draw()
    L2.draw()
    pygame.display.set_caption("Multiplayer_Tic_Tac_Toe")
    pygame.display.flip()