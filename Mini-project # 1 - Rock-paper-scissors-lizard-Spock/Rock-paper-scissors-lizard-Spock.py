# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    if name == "rock" :
        return 0
    elif name == "Spock" :
        return 1
    elif name == "paper" :
        return 2
    elif name == "lizard" :
        return 3
    elif name == "scissors" :
        return 4
    else :
        print "No such name possible" 
     


def number_to_name(number):
    # delete the follwing pass statement and fill in your code below
    if number == 0 :
        return "rock"
    elif number == 1 :
        return "Spock" 
    elif number == 2 :
        return "paper"
    elif number == 3 :
        return "lizard"
    elif number == 4 :
        return "scissors"
    else :
        print "No such number possible"
        
    

def rpsls(player_choice): 
    # delete the follwing pass statement and fill in your code below
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5);
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice;
    difference = (comp_number - player_number) % 5
    
    if difference==0:
        print "Player and computer tie!"
    elif difference==4 or difference==3:
        print "Player wins!"
    elif difference==1 or difference==2:
        print "Computer wins!"
    else:
        print "Wrong input!"
    print
        
     
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


