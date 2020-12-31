import turtle
import os
import math
import random 
from copy import deepcopy
import numpy as np

global Move_list 
Move_list = []
# Use https://trinket.io/features/pygame to convert this to an online embedded game, when the 
# Website is up
#Webflow 

#Setting up initial gameplay variables

# sc = turtle.Screen() 
# sc.setup(600, 600) 
 
# #TODO ---make so if player hits square that is already hit, it will prompt to hit new square, and not give error

# Variable8= ""
# Choice3 = False
# while Choice3 == False:
#     list_words = ["yes", "no"]
#     Variable8 = input("Play vs computer? Enter yes, or no: \n")
#     # Variable8 = turtle.textinput("Play vs computer?",  "Enter yes, or no")
#     if Variable8 in list_words:
#         Choice3 = True
#         Variable8 = Variable8

# if Variable8 == "no":


#     Variable1 = 580
#     Var2 = 0
#     Choice = False
#     while Choice == False:
#         list_nums = str([i for i in range(3,21)])
#         # Variable2 = turtle.textinput("Dimensions of Board ",  "Enter Rows from 3-20 inclusive")
#         Variable2 = input("Dimensions of Board?  Enter Rows from 3-20 inclusive: \n")
#         # Variable2 = (input("Please enter how many rows and columns you wish the board to have. Input needs to be an integer between 3 and 25, inclusive: \n"))
#         #Force user input to be in list of values, while not breaking program if they type a string
#         if Variable2 != '':
#             if Variable2 in list_nums:
#                 Var2 = int(Variable2)    
#                 Choice = True
    
#     Variable2 = Var2        
#     Variable3 = int(Variable2) ** 2

#     Choice2 = False
#     while Choice2 == False:
        
            
#         if Var2 == 3:
#             list_nums2 = str([3])
#             # print("I am a 3")
#         elif Var2 == 4:
#             list_nums2 = str([4])
#         elif Var2 == 5:
#             list_nums2 = str([5])
#             # print("I am a 5")
#         elif Var2 == 6:
#             list_nums2 = str([6])
#         elif Var2 == 7:
#             list_nums2 = str([5, 6, 7])
        
#         elif Var2 > 7:
#             list_nums2 = str([i for i in range(3, (Var2 + 1))])
        
        
#         # Variable4 = turtle.textinput("Required number of tiles to win ",  "Enter consecutive squares needed to win")
        
#         choice3 = False
#         while choice3 == False:
#             if Variable2 <=6:
#                 print(f"You must choose {Variable2} tiles needed to win")
#             elif Variable2 == 7:
#                 print(f"You can choose 5,6, or 7 tiles needed to win")    
#             else:
#                 print(f"You must choose between {math.ceil(Variable2/2)} and {Variable2} tiles needed to win, inclusive.")
#             Variable4 = input("Required number of tiles to win ? Enter consecutive squares needed to win: \n")
            
#             list_nums2 = str([i for i in range(3,21)])
#             if Variable4 != '':
#                 if Variable4 in list_nums2:
#                     Variable4 = int(Variable4)
#                     choice3 = True  
        
        
#         Variable4 = int(Variable4)
        
#             #Force user input to be in list of values, while not breaking program if they type a string
#         if Var2 > 7:
#             if Variable4 <= Var2 and Variable4 > (.5* Var2):
#                 Choice2 = True  
#         if Var2 <=6:
#             if Variable4 == Var2:
#                 Choice2 = True
#         if Var2 == 7:
#             if Variable4 >=5 and Variable4 <=7:
#                 Choice2 = True

# if Variable8 == "yes":

#         Variable1 = 580
#         Var2 = 0
#         Choice = False
#         while Choice == False:
#             list_nums = str([i for i in range(3,21,2)])
#             # Variable2 = turtle.textinput("Dimensions of Board ",  "Enter Rows from 3-20 inclusive, Odd #s Only")
#             Variable2 = input("Dimensions of Board ? Enter Rows from 3-20 inclusive, Odd #s Only: \n")
#             # Variable2 = (input("Please enter how many rows and columns you wish the board to have. Input needs to be an integer between 3 and 25, inclusive: \n"))
#             #Force user input to be in list of values, while not breaking program if they type a string
#             if Variable2 != '':
#                 if Variable2 in list_nums:
#                     Var2 = int(Variable2)    
#                     Choice = True
    
#         Variable2 = Var2   
                
#         Variable3 = int(Variable2) ** 2
#         #if Variable4 <= Variable2 and Variable4 > (.5* Variable2):
#         Choice2 = False
#         while Choice2 == False:
            
               
#             if Var2 == 3:
#                 list_nums2 = str([3])
#                 # print("I am a 3")
#             elif Var2 == 4:
#                 list_nums2 = str([4])
#             elif Var2 == 5:
#                 list_nums2 = str([5])
#                 # print("I am a 5")
#             elif Var2 == 6:
#                 list_nums2 = str([6])
#             elif Var2 == 7:
#                 list_nums2 = str([5, 6, 7])
            
#             elif Var2 > 7:
#                 list_nums2 = str([i for i in range(3, (Var2 + 1))])
            
            
#             # Variable4 = turtle.textinput("Required number of tiles to win ",  "Enter consecutive squares needed to win")
            
#             choice3 = False
#             while choice3 == False:
#                 if Variable2 <=6:
#                     print(f"You must choose {Variable2} tiles needed to win")
#                 elif Variable2 == 7:
#                     print(f"You can choose 5,6, or 7 tiles needed to win")    
#                 else:
#                     print(f"You must choose between {math.ceil(Variable2/2)} and {Variable2} tiles needed to win, inclusive.")
#                 Variable4 = input("Required number of tiles to win ? Enter consecutive squares needed to win: \n")
#                 list_nums = str([i for i in range(3,21)])
#                 if Variable4 != '':
#                     if Variable4 in list_nums2:
#                         Variable4 = int(Variable4)
#                         choice3 = True 
            
            
#             Variable4 = int(Variable4)
            
#                 #Force user input to be in list of values, while not breaking program if they type a string
#             if Var2 > 7:
#                 if Variable4 <= Var2 and Variable4 > (.5* Var2):
#                     Choice2 = True  
#             if Var2 <=6:
#                 if Variable4 == Var2:
#                     Choice2 = True
#             if Var2 == 7:
#                 if Variable4 >=5 and Variable4 <=7:
#                     Choice2 = True

# Variable10a= ""
# Choice4 = False
# while Choice4 == False:
#     list_words = ["yes", "no"]
#     Variable10 = input("Play game till end? Enter yes, or no: \n")
#     # Variable10 = turtle.textinput("Play game till end?",  "Enter yes, or no")
#     if Variable10 in list_words:
#         Choice4 = True
#         Variable10a = Variable10



# computer = turtle.Turtle()
# computer.color("blue")
# computer.shape("square")
# computer.penup()
# computer.speed(0)
# computer.setposition(0, 0)
# computer.hideturtle()


def Create_Player_Custom_Commands(Boardsize, Squares):
    '''
    Setting up custom size movement and x,o drawings to implement player versus computer matches
    Input: Boardsize, Squares in total on board
    Output: Custom player controls for the specific board
    '''
    global is_done_with_player_move
    is_done_with_player_move = False
    Square_Length = round((Boardsize / np.sqrt(Squares)))
    #speed is used for how far player moves with keystroke
    speed = Square_Length

    player = turtle.Turtle()
    player.color("red")
    player.shape("triangle")
    player.penup()
    player.speed(0)
        
    Starting_pos_x = -(Boardsize/2) + .5*(Square_Length) + (((np.sqrt(Squares)-1)/2) * Square_Length)
    Starting_pos_y = (Boardsize/2) - .5*(Square_Length) - (((np.sqrt(Squares)-1)/2) * Square_Length)
    
    player.setposition(Starting_pos_x , Starting_pos_y )
    player.setheading(90)
    
    movement = (Boardsize/Squares)*1.5

    def move_left():
        
        x = player.xcor()
        x -= speed      
        
        if x < -(Boardsize/2)+ .5*(Square_Length):
            x = -(Boardsize/2)+ .5*(Square_Length)
        
        player.setx(x)
        player.setpos(x, player.ycor())
        
    def move_right():
        x = player.xcor()
        x += speed
        if x > (Boardsize/2) - .5*(Square_Length):
            x = (Boardsize/2) - .5*(Square_Length)
        player.setx(x)
        player.setpos(x, player.ycor())
        
    def move_up():
        y = player.ycor()
        y += speed
        if y >  (Boardsize/2) - .5*(Square_Length):
            y = (Boardsize/2) - .5*(Square_Length)
        player.sety(y)
        player.setpos(player.xcor(), y)
        
    def move_down():
        y = player.ycor()
        y -= speed
        if y < -(Boardsize/2)+ .5*(Square_Length):
            y = -(Boardsize/2)+ .5*(Square_Length)
        player.sety(y)
        player.setpos(player.xcor(), y)
            
    def draw_circle():
        turtle.pensize(2.5)
        a = player.xcor()
        b = player.ycor()
        
        coord_value = [a, b]
                
        turtle.hideturtle()
        turtle.penup()
        turtle.setpos(a, (b-movement))

        turtle.pendown()
        turtle.circle(movement)
        turtle.hideturtle()

            
    def draw_x():
        turtle.pensize(2.5)
        a = player.xcor()
        b = player.ycor()
        turtle.hideturtle()
        turtle.penup()
        
        coord_value = [a, b]
            
        turtle.setposition(a-movement,b+movement)
        turtle.pendown()
        turtle.setposition(a+movement,b-movement)
        turtle.penup()
        turtle.setposition(a-movement,b-movement)
        turtle.pendown()
        turtle.setposition(a+movement,b+ movement)
        # print(coord_value)

        global Player_COORD 
        Player_COORD = coord_value
               
        is_done_with_player_move = True
                    
    
    turtle.listen()
    turtle.onkey(move_left, "Left") 
    turtle.onkey(move_right, "Right")
    turtle.onkey(move_up, "Up") 
    turtle.onkey(move_down, "Down")
    # turtle.onkey(draw_circle, "o") 
    turtle.onkey(draw_x, "x") 


def Create_Board(Boardsize, Squares, Screen_Color, Screen_Title, Line_Color, Line_Size):
    '''
    This function creates the board based on custom boardsize, squares, etc
    '''

    Total_Horizontal_Lines = (math.sqrt(Squares)-1)
    Total_Vertical_Lines = (math.sqrt(Squares)-1)

    Total_Vertical_Distance = Boardsize 
    Total_Horizontal_Distance = Boardsize
    Distance_in_Between_Lines = (Boardsize / math.sqrt(Squares))
    #Have to implement Coordinate system
    First_Vertical_Line_X_Coords = -(Boardsize/2) + Distance_in_Between_Lines 
    First_Vertical_Line_Y_Coords = (Boardsize/2)
    First_Horizontal_Line_X_Coords = -(Boardsize/2)
    First_Horizontal_Line_Y_Coords = (Boardsize/2) - Distance_in_Between_Lines

    screen = turtle.Screen()          
    screen.screensize(Boardsize,Boardsize)
    screen.bgcolor(Screen_Color) 
    screen.title(Screen_Title)  

    Remaining_lines = Total_Vertical_Lines
    Current_X = First_Vertical_Line_X_Coords
    Current_Y = First_Vertical_Line_Y_Coords
    
    while Remaining_lines > 0:
                
        border_pen = turtle.Turtle()
        border_pen.speed(0)
        border_pen.color(Line_Color)
        border_pen.penup()
        border_pen.setposition(Current_X, Current_Y)
        border_pen.pendown()
        border_pen.pensize(Line_Size)
        border_pen.setheading(270)
        border_pen.fd(Boardsize)
        border_pen.hideturtle

        Current_X += Distance_in_Between_Lines
        Remaining_lines -=1 
    
    
    Remaining_lines = Total_Horizontal_Lines
    Current_X = First_Horizontal_Line_X_Coords
    Current_Y = First_Horizontal_Line_Y_Coords
    
    while Remaining_lines > 0:
        
        border_pen = turtle.Turtle()  
        border_pen.speed(0)
        border_pen.color(Line_Color)
        border_pen.penup()
        border_pen.setposition(Current_X, Current_Y)
        border_pen.pendown()
        border_pen.pensize(Line_Size)
        border_pen.setheading(0)
        border_pen.fd(Boardsize)
        border_pen.hideturtle()

        Current_Y -= Distance_in_Between_Lines
        Remaining_lines -=1 
    
   
def create_key_dict_and_coords(Boardsize, Squares):
    '''
    This function takes Boardsize, number of Squares, creates a list of each Square as a key, 
    and the key's value corresponds to an [X, Y, coordinate] list, returns a dictionary
    '''
    Name_of_Spots = list(range(0, Squares))
    Square_Length = round((Boardsize / np.sqrt(Squares)))
    Mid_Square_Length = (Square_Length / 2)
    Max_X_Coordinate = (Boardsize/2) - Mid_Square_Length
    Min_Y_Coordinate = -(Boardsize/2) + Mid_Square_Length 

    Coordinate_list = []
        
    Len_Coordinate_list = len(Name_of_Spots)
    Starting_X_Coordinate = -(Boardsize/2) + Mid_Square_Length
    Starting_Y_Coordinate = (Boardsize/2) - Mid_Square_Length
    
    X_coord = (Starting_X_Coordinate)
    Y_coord = (Starting_Y_Coordinate)
        
    while Len_Coordinate_list > 0:
        
        Individ_coord = []
        Individ_coord.append(X_coord)
        Individ_coord.append(Y_coord)
        
        Len_Coordinate_list -=1
        Coordinate_list.append(Individ_coord)


        if Len_Coordinate_list % int(math.sqrt(Squares)) == 0:
            X_coord = Starting_X_Coordinate
            Y_coord -= Square_Length
            

        elif Len_Coordinate_list % int(math.sqrt(Squares)) != 0:
            X_coord += Square_Length


    Key_Dict = dict(zip(Name_of_Spots, Coordinate_list))
    # print(Key_Dict)
    return Key_Dict 

def create_remaining_dict(Squares, Squares_to_win):
    
    '''
    Takes in total squares on the board and squares needed to win
    Returns a dictionary of all potential winning lines as keys, and how many consecutive squares
    are needed to win as their values
    '''

    Matrix = []
    list_size = int(np.sqrt(Squares))
    starting = 0
    ending = int(np.sqrt(Squares))
    len_matrix = Squares
    
    while len_matrix > 0:
        list_to_add = []

        for i in range(starting, ending):
            list_to_add.append(i)
       
        Matrix.append(list_to_add)
        starting += list_size 
        ending += list_size
        len_matrix -= list_size 
    #Winning_Lines represents all possible winning lines in the grid
        
    Winning_Lines = []
    Horizontal_lines_in_Matrix = int(math.sqrt(Squares))
        
    Total_Squares = 0
    smaller_list = []
    Row_index = 0
    Column_Idx = 0
    Total_Rows = Horizontal_lines_in_Matrix
    Total_Squares_per_iteration = int(Squares_to_win)
    Iterations_per_row = int(math.sqrt(Squares)-Squares_to_win)+1
    Starting_Column = 0
    Starting_Row = 0
    
    while Horizontal_lines_in_Matrix > 0:
                
        while Total_Squares < (Total_Squares_per_iteration * Iterations_per_row * Horizontal_lines_in_Matrix):
            
            smaller_list.append(Matrix[Row_index][Column_Idx])
                       
            Column_Idx +=1
            Total_Squares +=1

            #When we come back to this loop, we start off where we last were, only 1 row lower
                    
            if Total_Squares == (Total_Squares_per_iteration * Iterations_per_row) :
                a = smaller_list[:]
                # print(a)
                Winning_Lines.append(a)
                smaller_list.clear()
                Starting_Row +=1
                Row_index = Starting_Row
                Total_Squares = 0
                Horizontal_lines_in_Matrix -=1
                Starting_Column = 0
                Column_Idx = Starting_Column
                break 
            
            if Total_Squares % Total_Squares_per_iteration == 0:
                b = smaller_list[:]
                Winning_Lines.append(b)
                smaller_list.clear()
                Starting_Column +=1
                Column_Idx = Starting_Column
                
                break 


    Vertical_lines_in_Matrix = math.sqrt(Squares)            
    Total_Squares = 0
    smaller_list = []
    Row_index = 0
    Column_Idx = 0
    Total_Columns = Vertical_lines_in_Matrix 
    Total_Squares_per_iteration = int(Squares_to_win)
    Iterations_per_row = int(math.sqrt(Squares)-Squares_to_win)+1
    Starting_Column = 0
    Starting_Row = 0
    
    while Vertical_lines_in_Matrix > 0:
        
        while Total_Squares < (Total_Squares_per_iteration * Iterations_per_row * Vertical_lines_in_Matrix):

                
            smaller_list.append(Matrix[Row_index][Column_Idx])
                        
            Row_index +=1
            Total_Squares +=1
                               
            if Total_Squares == (Total_Squares_per_iteration * Iterations_per_row) :
                a = smaller_list[:]
                Winning_Lines.append(a)
                smaller_list.clear()
                Starting_Column +=1
                Column_Idx = Starting_Column
                Total_Squares = 0
                Vertical_lines_in_Matrix -=1
                Starting_Row = 0
                Row_index = Starting_Row
                break 
            
            if Total_Squares % Total_Squares_per_iteration == 0:
                b = smaller_list[:]
                Winning_Lines.append(b)
                smaller_list.clear()
                Starting_Row +=1
                Row_index = Starting_Row
                
                break
    
    Rows_to_iterate_using_Diagonals = int(1 + (math.sqrt(Squares)-Squares_to_win)) 
    Iterations_per_row_using_Diagonals = 1 + (math.sqrt(Squares)-Squares_to_win) 
    Total_Squares_per_iteration = int(Squares_to_win) 

    Total_Rows = int(Rows_to_iterate_using_Diagonals)
    smaller_list = []
    Total_Squares = 0
    Row_index = 0
    Column_Idx = 0
    Starting_Column = 0
    Starting_Row = 0

    while Rows_to_iterate_using_Diagonals > 0:
               
        while Total_Squares < (Total_Squares_per_iteration * Iterations_per_row_using_Diagonals* Rows_to_iterate_using_Diagonals):
                   
            smaller_list.append(Matrix[Row_index][Column_Idx])
                        
            Row_index +=1
            Column_Idx +=1
            Total_Squares +=1
                                
            if Total_Squares == (Total_Squares_per_iteration * Iterations_per_row_using_Diagonals) :
                a = smaller_list[:]
                Winning_Lines.append(a)
                smaller_list.clear()
                Starting_Row +=1
                Row_index = Starting_Row
                Starting_Column = 0
                Column_Idx = Starting_Column
                Total_Squares = 0
                Rows_to_iterate_using_Diagonals -=1
                break 
            
            if Total_Squares % Total_Squares_per_iteration == 0:
                b = smaller_list[:]
                Winning_Lines.append(b)
                smaller_list.clear()
                Starting_Column +=1
                Column_Idx = Starting_Column
                Row_index = Starting_Row

                break 
           
    Rows_to_iterate_using_Diagonals = int(1 + (math.sqrt(Squares)-Squares_to_win)) 
    Iterations_per_row_using_Diagonals = 1 + (math.sqrt(Squares)-Squares_to_win) 
    Total_Squares_per_iteration = int(Squares_to_win) 

    Total_Rows = int(Rows_to_iterate_using_Diagonals)
    smaller_list = []
    Total_Squares = 0
    Row_index = int(math.sqrt(Squares)-1)
    Column_Idx = 0
    Starting_Column = 0
    Starting_Row = int(math.sqrt(Squares)-1)

    
    while Rows_to_iterate_using_Diagonals > 0:
                
        while Total_Squares < (Total_Squares_per_iteration * Iterations_per_row_using_Diagonals* Rows_to_iterate_using_Diagonals):
                  
            smaller_list.append(Matrix[Row_index][Column_Idx])
                        
            Row_index -=1
            Column_Idx +=1
            Total_Squares +=1
                   
            if Total_Squares == (Total_Squares_per_iteration * Iterations_per_row_using_Diagonals) :
                a = smaller_list[:]
                Winning_Lines.append(a)
                smaller_list.clear()
                Starting_Row -=1
                Row_index = Starting_Row
                Starting_Column = 0
                Column_Idx = Starting_Column
                Total_Squares = 0
                Rows_to_iterate_using_Diagonals -=1
                break 
            
            if Total_Squares % Total_Squares_per_iteration == 0:
                b = smaller_list[:]
                Winning_Lines.append(b)
                smaller_list.clear()
                Starting_Column +=1
                Column_Idx = Starting_Column
                Row_index = Starting_Row

                break 
           

    Count_Lists = [Squares_to_win] * len(Winning_Lines)
    Winning_Lines_Tuples =  [tuple(x) for x in Winning_Lines]

    Remaining_dict = dict(zip(Winning_Lines_Tuples, Count_Lists))    
    return Remaining_dict

def create_Dictionary_List(Squares, Squares_to_win, Number_of_Computer_Players):
    #We are going to create a Dictionary list for all players, and an opponent will basically reference all other keys in 
    # the dictionary that do not have his name as the key, this will then be the opponent dictionary, and he will access
    #his name as key, for his Own dictionary
    Individual_Dict = create_remaining_dict(Squares**2, Squares_to_win)
    
    Computer_player_count = Number_of_Computer_Players
    Computer_Names = ['red square', 'blue square', 'green square', 'red circle', 'blue circle', 'green circle']
    
    comp_list = []
    for i in range (0,Computer_player_count):
        x = Computer_Names[i]
        comp_list.append(x)

    #This represents each player and their corresponding dictionary
    List = []
    Nested_dict_list = []
    for i in comp_list:
        List.append(Individual_Dict)

    Nested_dict_list = dict(zip(comp_list, List))   
    
    return Nested_dict_list     
    #Have to add this to a list
      


    
def neighbors(Matrix, row, column):
    '''
    Helper function for the adjacency function. Finds all neighbors of each spot on the board,
    for a given spot. Sorts their values and returns the list of neighbors.
    '''
    
    Neighbors = []
    len_matrix = len(Matrix)-1
    

    if column < len_matrix:
        e = Matrix[row][column+1]
        Neighbors.append(e)
    if column < len_matrix and row > 0:
        c = Matrix[row-1][column+1]
        Neighbors.append(c)
    if column > 0:
        d = Matrix[row][column-1]
        Neighbors.append(d)
    if column > 0 and row > 0:
        a = Matrix[row-1][column-1]
        Neighbors.append(a)
    if row > 0:
        b = Matrix[row-1][column]
        Neighbors.append(b)
    if row < len_matrix:
        g = Matrix[row+1][column]
        Neighbors.append(g)
    if row < len_matrix and column < len_matrix:
        h = Matrix[row+1][column+1]
        Neighbors.append(h)
    if row < len_matrix and column > 0:
        f = Matrix[row+1][column-1]
        Neighbors.append(f)
    
    Neighbors.sort()    
    
    return Neighbors                

def Adjacency_Dict(Squares):
    '''
    Returns dictionary of individual squares as keys, and their adjacent spots on the board
    as values.
    '''
    #Create the Matrix from the Squares
    Matrix = []
    list_size = int(np.sqrt(Squares))
    starting = 0
    ending = int(np.sqrt(Squares))
    len_matrix = Squares
    
    while len_matrix > 0:
        list_to_add = []

        for i in range(starting, ending):
            list_to_add.append(i)
       
        Matrix.append(list_to_add)
        starting += list_size 
        ending += list_size
        len_matrix -= list_size

    a = int(len(Matrix))

    x= 0
    y= 0

    Adjacency_list = []

    while a > 0:
        
        output = neighbors(Matrix,x,y)
        Adjacency_list.append(output)

        y+=1

        if y == len(Matrix):
            y = 0
            x+=1
            a-=1


    Name_of_Squares = list(range(0, Squares))    
    Adjacency_dict = dict(zip(Name_of_Squares, Adjacency_list))    
    
    return(Adjacency_dict)    



def comp_draw_customized_x(boardsize, squares):
    '''
    Creates customized shape drawing of x for the computer based on the boardsize and squares 
    on the board.
    '''
    turtle.pensize(2.5)
    turtle.color("blue")
    a = computer.xcor()
    b = computer.ycor()
    turtle.hideturtle()
    turtle.penup()

    coord_value = [a, b]
    
    movement = (boardsize/squares)*1.5

    turtle.setposition(a-movement,b+movement)
    turtle.pendown()
    turtle.setposition(a+movement,b-movement)
    turtle.penup()
    turtle.setposition(a-movement,b-movement)
    turtle.pendown()
    turtle.setposition(a+movement,b+ movement)

    return coord_value 

def computer_draw_customized_circle(boardsize, squares):
    '''
    Creates customized shape drawing of circle for the computer based on the boardsize and squares 
    on the board.
    '''
    movement = (boardsize/squares)*1.5
    
    turtle.pensize(2.5)
    turtle.color("red")
    a = computer.xcor()
    b = computer.ycor()

    coord_value = [a, b]
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(a, (b-movement))
    
    turtle.pendown()
    turtle.circle(movement)
    turtle.hideturtle()

    return coord_value 

def create_updated_dictionary(Remaining_dict, Squares_to_win):
    '''
    Creates an updated dictionary 
    '''
    
    X_list = ["winning_lines", "opponent_winning_lines", "sum_of_remaining_lines", "Can_increase_winning_lines", "Can_lower_opponent_lines"]
    X_list2 = [0, 0, (len(Remaining_dict) * Squares_to_win), True, True]

    Updated_Dict = dict(zip(X_list, X_list2))
    return Updated_Dict

def key_name(dictionary, coordinate):
    '''
    Finds particular key based on the given coordinate.
    '''
    for key, value in dictionary.items():
        if value == coordinate:
            position = key
    return position        

def decrease_values(dictionary, key_name, updated_dictionary):
    '''
    Takes in a key, and reduces all winning line values that contain that key.
    '''
    list_of_keys = []
    for key, value in dictionary.items():
        for keys in key:
            if key_name == keys:
                list_of_keys.append(key)
    for winning_line in list_of_keys:
        for key in dictionary.keys():
            if winning_line == key:
                dictionary[winning_line] = dictionary[winning_line]-1
    
    Count = 0
    for values in dictionary.values():
        Count +=values 
    updated_dictionary["sum_of_remaining_lines"] = Count 
        

    Values = []
    for value in dictionary.values():
        Values.append(value)
           
    if min(Values) == 0:
        return 0 
    else:
        return dictionary   

def decrease_values_multiple_players(dictionary, key_name):
    '''
    Takes in a key and reduces all winning lines in multiple player game
    '''                            

    
    for value in dictionary.values():
        for key_lists in value.keys():
            
            if key_name in key_lists:
                value[key_lists] = value[key_lists]-1
    Values = []            
    for value in dictionary.values():
        for valuez in value.values():
            Values.append(valuez)
    if min(Values) == 0:
        return 0
    else:
        return dictionary                         


def remove_dict(Key_Dictionary,  coordinate):
    '''
    Removes the key from the dictionary if the coordinate corresponds to the key. 
    '''
        
    for key,value in Key_Dictionary.items():
        if value == coordinate:
            storedvalue = key
    Key_Dictionary.pop(storedvalue)
    return Key_Dictionary


#    move_list = []
#    for key,value in Key_Dictionary.items():
#        if value == coordinate:
#            move_list.append(key)

# We need to define a way to reference all opponent dictionaries, we will reference the key dictionary and the pieces removed
#from the key dictionary will go into the list of moves, which will be one general list
#So all dictionaries will be referenced through a for loop, so we need a way to get all opponent dictionaries into one, we
#Can nest them 

def Divide_Dictionary(Dictionary, Player):
    Player_Name = []
    Player_Values = []
    Opponent_Names = []
    Opponent_Values = []
    for k,v in Dictionary.items():
        if k == Player:
            Player_Name.append(k)
            Player_Values.append(v)
        elif k != Player:
            Opponent_Names.append(k)
            Opponent_Values.append(v)

    Player_Dict = dict(zip(Player_Name, Player_Values))
    Opponent_Dict = dict(zip(Opponent_Names, Opponent_Values))

    return  Player_Dict, Opponent_Dict        





def Multiple_Terminator_Move(Player_Piece, Dictionary_List, Key_Dictionary, Starting_count, \
    Adjacency_Dict, List_of_Moves):
    '''
    This is the brain of the game. It is the algorithm behind the computer's moves and logic.
    This is meant for multiple AI players
    '''
    #Key dictionary, list of keys and their positions---Already created

    #def create_Dictionary_List(Squares, Squares_to_win, Number_of_Computer_Players)
    
    #Adjacency Dict-Already created

    #Computer_Piece_List = ['red square', 'blue square', 'green square', 'red circle', 'blue circle', 'green circle']

    #Ideas
    # Each computer player needs to be able to access all winning lines of all other players including
    # itself 


    # We will need the computer's color and x or circle mark, to identify the computer 
    # Has to be able to reference itself
    # 
    #  
    # Instead of using each player's list of moves, we are going to use one general list
    # So when the computer makes their move, and when we remove the key from the key dictionary, 
    # We need to place that key in a list, which we will reference here
    #
    #    move_list = []
    #    for key,value in Key_Dictionary.items():
    #        if value == coordinate:
    #            move_list.append(key)
    #    
    #    at the end of each computer player's turn, they will append the key through this function to
    #    the global move_list, and we can then reference this list in our function   
    #
    #    Accessing the Dictionary List, Adjacency_Dict, List_of_Moves, Your_Dictionary,
    #    will be the way it evaluates
    #
    
    

    Player_Dict = Divide_Dictionary(Dictionary_List, Player_Piece)[0]
    Opponent_Dict = Divide_Dictionary(Dictionary_List, Player_Piece)[1]

    #Divide the Dictionary into separate components, to operate more efficiently on

    #Going to be referencing this throughout the function  


     






    List_of_Moves = Move_list

    #Remaining Keys represents possible spots to move to in any given move
    Remaining_Keys = []
    for key in Key_Dictionary.keys():
        Remaining_Keys.append(key)
       
    #This check makes sure, first, that you block opponent's move, puts key to remove in Keys_to_Remove list
    Keys_to_Remove = []
    for winning_line, count in Opponent_Dictionary_List.items():
        for Line, Count in Your_Dictionary.items():
            if winning_line == Line:
                if count == 1 and Count == Starting_count:
                    for keys in Line:
                        if keys in Remaining_Keys:
                            Keys_to_Remove.append(keys)
       
    #Setting up winning move if possible:
    Keys_to_win = []
    for winning_line, count in Opponent_Dictionary.items():
        for Line, Count in Your_Dictionary.items():
            if Line == winning_line:
                if Count == 1 and count == Starting_count:
                    for keys in Line:
                        if keys in Remaining_Keys:
                            Keys_to_win.append(keys)
    #Check if you can win
    if len(Keys_to_win)> 0:
        for position, coord in Key_Dictionary.items():
            if Keys_to_win[0] == position:
                coordinates = coord
                computer.setpos(coordinates[0],coordinates[1])
                List_of_your_moves.append(Keys_to_win[0])
                return                          
    
    #Check if you MUST block winning move of opponent
    if len(Keys_to_Remove)> 0:
        for position, coord in Key_Dictionary.items():
            if Keys_to_Remove[0] == position:
                coordinates = coord
                computer.setpos(coordinates[0],coordinates[1])
                List_of_your_moves.append(Keys_to_Remove[0])
                return
       
    Keys_Remaining = len(Remaining_Keys)
    Winning_Line_Count = []
    Winning_lines_Containers = []
    Count = 0
    index = 0
    Special_Case_Count = 0
    Opp_winning_lines = []
    Your_winning_lines = []
    Opp_Adjacency_list = []
    Your_Adjacency_list = []
    while Keys_Remaining > 0:
        
        key = Remaining_Keys[index]
        #value winning lines highly to stop opponent, value count highly, super highly in the beginning, this is only
        #to block winning lines
        for Winning_lines, valuess in Your_Dictionary.items():
            for Winning_linez, valuezz in Opponent_Dictionary.items():
                if Winning_lines == Winning_linez:
                    if valuezz < Starting_count and valuess == Starting_count:
                        if key in Winning_lines:
                            Opp_winning_lines.append(key)
                            Special_Case_Count +=1
                            if valuess - valuezz <= .5 * Starting_count:
                                #Make incentive on smaller board to block quicker, as one slip up early can cost game
                                #Notice it is to the 8th power here, again bigger than continuing winning line, which is 
                                # only raised to the 6th power
                                if Starting_count <= 6:
                                    Count +=  (valuess - valuezz)**8
                                #Disincentivize blocking early on big boards, no need, better to expand
                                elif Starting_count > 6:
                                    Count +=  (valuess - valuezz)**2

                            elif valuess - valuezz > .5 * Starting_count:
                                #Not as important to block once it's too late in small games, by that point, it should have 
                                #already blocked, but still more value than adjacency moves
                                if Starting_count < 6:
                                    Count +=  (valuess - valuezz)**7
                                #Make the incentive on a bigger board, to wait until blocks are >half the amount to win
                                #Before you force the block, allow for more expansion...notice its to the 7th power here,
                                # which makes it more important than continuing your original line, which is only raised to 6th
                                elif Starting_count > 6:
                                    Count +=  (valuess - valuezz)**7

        #improve your winning line if possible, value count highly, this is only to improve existing winning lines
        for Winning_lines, values in Opponent_Dictionary.items():
            for Winning_linez, valuez in Your_Dictionary.items():
                if Winning_lines == Winning_linez:
                    if valuez < Starting_count and values == Starting_count:
                        if key in Winning_lines:
                            Your_winning_lines.append(key)
                            Special_Case_Count +=1
                            #incentivizing continuing the winning lines in progress on any board size, 
                            #This incentivizes expanding on early winning lines
                            if values - valuez < .5 * Starting_count:
                                Count += (valuess - valuezz)**6
                            #After blocking opponents early lines in small games, or late lines in big games, 
                            # raising to the power of 4 here trumps the 3rd and 2nd power in the other games, 
                            # meaning this will take precendence over blocking in those situations
                            elif values - valuez >= .5 * Starting_count:
                                Count +=  (values - valuez)**4
        #We need something to implement finding new winning lines
        for Winning_lines, values in Opponent_Dictionary.items():
            for Winning_linez, valuez in Your_Dictionary.items():
                if Winning_lines == Winning_linez:
                    if values == Starting_count and valuez == Starting_count:
                        if key in Winning_lines:
                            Special_Case_Count +=1
                            count += Starting_count        
        
        #Value 2nd highly if spot is in adjacency Dict of opponent moves
        for keys, adjacency_list in Adjacency_Dict.items():
            for keyz in List_of_Opponent_Moves:
                if keyz == keys:
                    if key in adjacency_list:
                        Opp_Adjacency_list.append(key)
                        Special_Case_Count +=1

                        Count +=len(adjacency_list)
        #Value 2nd highly if spot is in adjacency Dict of your moves
        for ky, adj_list in Adjacency_Dict.items():
            for kyz in List_of_your_moves:
                if kyz == ky:
                    if key in adj_list:
                        Your_Adjacency_list.append(key)
                        Special_Case_Count +=1
                        Count +=len(adjacency_list)              
        
        #Added bonuses, exponential bonus, based on how many of the previous conditions it meets          
        Count += (Special_Case_Count**2)
        #Most of the time, this special case count will not matter, until winning lines and blocking come to an end,
        # At which case you will see players only playing adjacent, because of the small added incentive      
        
        #Append the count, clear all the containers, repeat
        Winning_Line_Count.append(Count)
        Count = 0
        Special_Case_Count = 0 
        Opp_winning_lines.clear()
        Your_winning_lines.clear()
        Opp_Adjacency_list.clear()
        Your_Adjacency_list.clear()
        Winning_lines_Containers.clear()        
        index +=1
        Keys_Remaining -=1

    Best_Choice = dict(zip(Remaining_Keys, Winning_Line_Count))
    Random_Final_Choiz = []
    Random_Best_Choice = []
    Random_Key = []    
    for key, value in Best_Choice.items():
        Random_Best_Choice.append(value)
    
    max_val = max(Random_Best_Choice)
            
    for key, value in Best_Choice.items():
        if value == max_val:
            Random_Key.append(key)
   
    if len(Random_Key) > 1:
        random_guy = random.randint(0, (len(Random_Key)-1))
        Random_Final_Choiz.append(Random_Key[random_guy])
        
        for position, coord in Key_Dictionary.items():
            if Random_Final_Choiz[0] == position:
                coordinates = coord 

                computer.setpos(coordinates[0],coordinates[1])
                List_of_your_moves.append(Random_Final_Choiz[0])
                return     
    
    Best_Key = max(Best_Choice, key=Best_Choice.get)
    for position, coord in Key_Dictionary.items():
        if Best_Key == position:
            coordinates = coord 

    computer.setpos(coordinates[0],coordinates[1])
    List_of_your_moves.append(Best_Key)
    return


global PLAYER_TURN
PLAYER_TURN = True
def Play_Game(Boardsize, Squares, Squares_to_win, Player=False,):
    '''
    Function to play entire game using all other functions. One ring, to rule them all!
    '''
    
    Create_Board(Boardsize, Squares, "white", "Tic-Tac-Toe", "black", 2.5)
    Key_Dictionary = create_key_dict_and_coords(Boardsize, Squares)
    Remaining_Dict_O = create_remaining_dict(Squares, Squares_to_win)
    Remaining_Dict_X = create_remaining_dict(Squares, Squares_to_win)
    Adjacency_Dict1 = Adjacency_Dict(Squares)
    List_of_X_moves = []
    List_of_O_moves = []
    Updated_Dict = create_updated_dictionary(Remaining_Dict_O, Squares_to_win)
    #If the computers are playing versus themselves:
    if Player==False:

        Count = 0

        random_start = random.randint(0,1)
        if random_start == 0:
            Variable = 1
        else:
            Variable = -1  

        Game_over = False
        while Count <Squares and Game_over == False:
                    
            while Variable  == 1:
                Terminator_Move(Remaining_Dict_O, Remaining_Dict_X, Key_Dictionary, Squares_to_win, List_of_X_moves, List_of_O_moves,\
                    Adjacency_Dict1)
                Coordinat = (computer_draw_customized_circle(Boardsize, Squares))
                key = (key_name(Key_Dictionary, Coordinat))
                
                if decrease_values(Remaining_Dict_O, key, Updated_Dict) == 0:
                    print("O WINS!!!")
                    Game_over = True 
                    break
                                
                remove_dict(Key_Dictionary, Coordinat)
                
                if Variable10a == "no":
                    
                    Winning_line_O_counts= []
                    Winning_line_X_counts = []    
                    for value in Remaining_Dict_O.values():
                        Winning_line_O_counts.append(value)
                    for value in Remaining_Dict_X.values():
                        Winning_line_X_counts.append(value)    
                    
                    max_val_O = max(Winning_line_O_counts)
                    max_val_X = max(Winning_line_X_counts)
                    
                    if max_val_O < Squares_to_win and max_val_X < Squares_to_win:
                        print("The game can no longer be won!")
                        turtle.textinput("The game can no longer be won! ", "Press Stop to restart the game")
                        turtle.bye()
                                    
                Variable *= -1
                Count +=1
                
                if Count == Squares:
                    break
            
            while Variable == -1:
                if Count == Squares:
                    break 
                                      
                Terminator_Move(Remaining_Dict_X, Remaining_Dict_O, Key_Dictionary, Squares_to_win, List_of_O_moves, List_of_X_moves,\
                   Adjacency_Dict1)
                Coordinat = (comp_draw_customized_x(Boardsize, Squares))
                key = (key_name(Key_Dictionary, Coordinat))
                
                if decrease_values(Remaining_Dict_X, key, Updated_Dict) == 0:
                    print("X WINS!!!")
                    Game_over = True 
                    break
                    
                remove_dict(Key_Dictionary, Coordinat)
                
                if Variable10a == "no":
                    
                    Winning_line_O_counts= []
                    Winning_line_X_counts = []    
                    for value in Remaining_Dict_O.values():
                        Winning_line_O_counts.append(value)
                    for value in Remaining_Dict_X.values():
                        Winning_line_X_counts.append(value)    
                    max_val_O = max(Winning_line_O_counts)
                    max_val_X = max(Winning_line_X_counts)
                    
                    if max_val_O < Squares_to_win and max_val_X < Squares_to_win:
                        print("The game can no longer be won!")
                        turtle.textinput("The game can no longer be won! ", "Press Stop to restart the game")
                        turtle.bye()    
                
                Variable *=-1
                Count +=1

                if Count == Squares:
                    break
    #If the player is interacting with the computer:    
    if Player==True:
        
        random_start = random.randint(0,1)
        if random_start == 0:
            Player=False
        else:
            Player=True  

        Game_over = False
                      
        while Game_over == False:
                                   
            while Player==False:
                Terminator_Move(Remaining_Dict_O, Remaining_Dict_X, Key_Dictionary, Squares_to_win, List_of_X_moves, List_of_O_moves,\
                    Adjacency_Dict1)
                Coordinat = (computer_draw_customized_circle(Boardsize, Squares))
                key = (key_name(Key_Dictionary, Coordinat))
                                
                if decrease_values(Remaining_Dict_O, key, Updated_Dict) == 0:
                    print("O WINS!!!")
                    Game_over = True
                                           
                remove_dict(Key_Dictionary, Coordinat)
                                
                Player=True
                          
            
            while Player==True:
                
                def switch_players():
                    '''
                    This function allows the player to use the prompt to finish their loop, 
                    go through the computers loop and end up back at their loop again.
                    This allows us to run the turtle commands while keeping the game open 
                    with minimum interruption.                                                           
                    '''
                    key = (key_name(Key_Dictionary, Player_COORD))
                    List_of_X_moves.append(key)
                    
                    if decrease_values(Remaining_Dict_X, key, Updated_Dict) == 0:
                        print("X WINS!!!")
                        turtle.textinput("X has won!", "Press Stop to restart the game")
                        turtle.bye()
                                    
                                        
                    remove_dict(Key_Dictionary, Player_COORD)
                   
                    #Check to see if game can no longer be won by either player  
                    if Variable10a == "no":

                        Winning_line_O_counts= []
                        Winning_line_X_counts = []    
                        
                        for value in Remaining_Dict_O.values():
                            Winning_line_O_counts.append(value)
                        for value in Remaining_Dict_X.values():
                            Winning_line_X_counts.append(value)    
                        
                        max_val_O = max(Winning_line_O_counts)
                        max_val_X = max(Winning_line_X_counts)
                        
                        if max_val_O < Squares_to_win and max_val_X < Squares_to_win:
                            print("The game can no longer be won!")
                            turtle.textinput("The game can no longer be won!", "Press Stop to restart the game")
                            turtle.bye()

                    Len_list = []
                    for key in Key_Dictionary.keys():
                        Len_list.append(key)
                    if len(Len_list) == 0:
                        print("Thanks for playing!")
                        turtle.textinput("Thanks for playing!", "Press Stop to restart the game")
                        turtle.bye()    
                                             

                    Terminator_Move(Remaining_Dict_O, Remaining_Dict_X, Key_Dictionary, Squares_to_win, List_of_X_moves, List_of_O_moves,\
                    Adjacency_Dict1)
                    Coordinat = (computer_draw_customized_circle(Boardsize, Squares))
                    
                    key = (key_name(Key_Dictionary, Coordinat))
                                        
                    if decrease_values(Remaining_Dict_O, key, Updated_Dict) == 0:
                        print("O WINS!!!")
                        turtle.textinput("O has won! ", "Press Stop to restart the game")
                        turtle.bye()
                    
                    list_o_keys = []                  
                    remove_dict(Key_Dictionary, Coordinat)
                                        
                    #Check to see if game can no longer be won by either player
                    if Variable10a == "no":
                    
                        Winning_line_O_counts= []
                        Winning_line_X_counts = []    
                        
                        for value in Remaining_Dict_O.values():
                            Winning_line_O_counts.append(value)
                        for value in Remaining_Dict_X.values():
                            Winning_line_X_counts.append(value)    
                        
                        max_val_O = max(Winning_line_O_counts)
                        max_val_X = max(Winning_line_X_counts)
                        
                        if max_val_O < Squares_to_win and max_val_X < Squares_to_win:
                            print("The game can no longer be won!")
                            turtle.textinput("The game can no longer be won! ", "Press Stop to restart the game")
                            turtle.bye()
                    
                    for key in Key_Dictionary.keys():
                        list_o_keys.append(key)
                    
                    if (len(list_o_keys)) == 0:
                        print("Thanks for playing!")
                        turtle.textinput("Thanks for playing! ", "Press Stop to restart the game")
                        turtle.bye()
                    
                    global PLAYER_TURN
                    PLAYER_TURN = True    
   
                Square_Length = round((Boardsize / np.sqrt(Squares)))
    
                speed = Square_Length

                player = turtle.Turtle()
                player.color("green")
                player.shape("triangle")
                player.penup()
                player.speed(0)
                player.shapesize(.8, .8, .8)
                                    
                Starting_pos_x = -(Boardsize/2) + .5*(Square_Length) + (((np.sqrt(Squares)-1)/2) * Square_Length)
                Starting_pos_y = (Boardsize/2) - .5*(Square_Length) - (((np.sqrt(Squares)-1)/2) * Square_Length)
                
                player.setposition(Starting_pos_x , Starting_pos_y )
                player.setheading(90)
                
                movement = (Boardsize/Squares)*1.5
                
                                
                def draw_x():
                    '''
                    This is the player interaction function. Will allow the player to mark an x
                    when it is his or her turn to move. Will force the player to be in an unmarked
                    spot before allowing the X to be marked. Will then loop into the switch_players
                    function.
                    '''
                    turtle.pensize(2.5)
                    a = player.xcor()
                    b = player.ycor()
                    turtle.hideturtle()
                    turtle.penup()
                    turtle.color("blue")
                    coord_value = [a, b]
                    
                    
                    list_of_Coords = []
                    
                    for key, coordinate in Key_Dictionary.items():
                        list_of_Coords.append(coordinate)
                    if coord_value in list_of_Coords:
                        
                        turtle.setposition(a-movement,b+movement)
                        turtle.pendown()
                        turtle.setposition(a+movement,b-movement)
                        turtle.penup()
                        turtle.setposition(a-movement,b-movement)
                        turtle.pendown()
                        turtle.setposition(a+movement,b+ movement)
                    
                        global Player_COORD 
                        Player_COORD = coord_value
                        global PLAYER_TURN
                        PLAYER_TURN = False
                        
                        switch_players()
                
                
                def move_left():
                    '''
                    Left command if it is the player's turn
                    '''
                    if PLAYER_TURN == True:

                        x = player.xcor()
                        x -= speed      
                        
                        if x < -(Boardsize/2)+ .5*(Square_Length):
                            x = -(Boardsize/2)+ .5*(Square_Length)
                        
                        player.setx(x)
                        player.setpos(x, player.ycor())
                    
                
                def move_right():
                    '''
                    Right command if it is the player's turn
                    '''
                    if PLAYER_TURN == True:

                        x = player.xcor()
                        x += speed
                        
                        if x > (Boardsize/2) - .5*(Square_Length):
                            x = -(Boardsize/2) + .5*(Square_Length) + ((np.sqrt(Squares)-1) * Square_Length)
                        
                        player.setx(x)
                        player.setpos(x, player.ycor())
                                    
                def move_up():
                    '''
                    Up command if it is the player's turn
                    '''
                    if PLAYER_TURN == True:

                        y = player.ycor()
                        y += speed

                        if y >  (Boardsize/2) - .5*(Square_Length):
                            y = (Boardsize/2) - .5*(Square_Length)
                        
                        player.sety(y)
                        player.setpos(player.xcor(), y)
                                    
                def move_down():
                    '''
                    Down command if it is the player's turn
                    '''
                    if  PLAYER_TURN == True:

                        y = player.ycor()
                        y -= speed
                        
                        if y < -(Boardsize/2)+ .5*(Square_Length):
                            y = (Boardsize/2) - .5*(Square_Length) - ((np.sqrt(Squares)-1) * Square_Length)
                        
                        player.sety(y)
                        player.setpos(player.xcor(), y)
                
                def quit_game():
                    '''
                    Allows player to quit game by pressing Esc at any time.
                    '''
                    turtle.textinput("See you later friend! ",  "Press Enter to quit")
                    turtle.bye()            
                                     
                
                turtle.listen()
                                
                turtle.onkey(move_left, "Left") 
                turtle.onkey(move_right, "Right")
                turtle.onkey(move_up, "Up") 
                turtle.onkey(move_down, "Down")
                # turtle.onkey(draw_circle, "o") 
                turtle.onkey(draw_x, "x")
                turtle.onkey(quit_game, "Escape")     

                turtle.mainloop()     
                            

                    
#This sets the main game loop using the prompts from the beginning
# If player chooses to play computer, use this loop                   
# if Variable8 == "yes":
#     print("Place mouse cursor over the board and click on the board to enable player controls. \n Move with the arrow keys, and mark your square with 'x' key ")
#     print("To restart the game, click the stop button, and then click run again.")
#     Play_Game(Variable1, Variable3, Variable4, Player=True)
# # If player chooses not to play computer, use this loop    
# if Variable8 == "no":
#     print("To restart the game, click the stop button, and then click run again.")
#     Play_Game(Variable1, Variable3, Variable4, Player=False)

A = create_Dictionary_List(3, 3, 6)
B = Divide_Dictionary(A, 'red square') 
print(B[0])
print(B[1])



