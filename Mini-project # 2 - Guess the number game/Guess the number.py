# template for Guess the number mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

# initialize global variables used in your code

secret_number = 0
number_of_guesses_left = 0
low = 0
high = 0

# helper function to start and restart the game

def new_game()
    global secret_number,number_of_guesses_left,low,high
    secret_number = random.randrange(low,high)
    number_of_guesses_left =int( math.ceil(math.log(high-low,2)))
    print New game. Range is from  + str(low) +  to   + str(high)
    print Number of remaining guesses is  + str(number_of_guesses_left)
    print  

# define event handlers for control panel
def range100()
    # button that changes range to range [0,100) and restarts
    global low,high
    low = 0
    high = 100
    new_game()
    
    
def range1000()
    # button that changes range to range [0,1000) and restarts
    global low, high
    low = 0
    high = 1000
    new_game()

def input_guess(guess)
    # main game logic goes here	
    global secret_number,number_of_guesses_left,low,high
    print Guess was  + guess
    guess = int(guess)
    if number_of_guesses_left = 0 
        number_of_guesses_left = number_of_guesses_left - 1
        print Number of remaining guesses is  + str(number_of_guesses_left)
        if secret_number == guess 
            print Correct!
            print  
            new_game()
        elif secret_number  guess 
            print Higher!
            print  
        else 
            print Lower!
            print  
    if number_of_guesses_left == 0 
        print  
        new_game()
        
    
# create frame

frame = simplegui.create_frame(New frame ,300,300)
# register event handlers for control elements
frame.add_button(Range is [0 , 100) , range100,100)
frame.add_button(Range is [0, 1000) , range1000 , 100)
frame.add_input(Guess , input_guess , 100)



# call new_game and start frame

frame.start()

# always remember to check your completed program against the grading rubric
