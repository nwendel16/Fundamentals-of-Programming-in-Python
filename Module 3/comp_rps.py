#Nick Wendel
#IT - 75
#9/20/29


import random
from random import randint
#create a list of play options
moves = ["rock", "paper", "scissors"]
  
#assign a random play to the computer
computer = moves[randint(0,2)]
  

player = input("Choose rock, paper, or scissors! ")     #Player inputs their choice
if player == computer:                                  #The rest of the code is comparing the player's 
    print(computer)                                     #answer to the computer's answer and determining
    print("Tie!")                                       #which response is appropriate
elif player == "rock":
    if computer == "paper":
        print(computer)                                 #This allows us to see the computer's choice
        print("You lose!", computer, "covers", player)
    else:
        print(computer)
        print("You win!", player, "smashes", computer)
elif player == "paper":
    if computer == "scissors":
        print(computer)
        print("You lose!", computer, "cut", player)
    else:
        print(computer)
        print("You win!", player, "covers", computer)
elif player == "scissors":
    if computer == "rock":
        print(computer)
        print("You lose...", computer, "smashes", player)
    else:
        print(computer)
        print("You win!", player, "cut", computer)
else:
    print("That's not a valid play. Check your spelling!")
