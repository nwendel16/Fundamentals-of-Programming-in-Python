import getpass

print("Step up and make your choice: Rock, Paper, Scissors. Don't show your opponent!\n") # Prints invitation verbiage
player1 = input("Player 1 : ")                                                            # Creates variable player1
player2 = input("Player 2 : ")                                                            # Creates variable player2
print("")

 
if (player1 == 'rock' and player2 == 'scissors'):           #Defines outcome if p1 plays rock and p2 plays scissors
    print ("Player 1 crushed Player 2.")
 
elif (player1 == 'rock' and player2 == 'rock'):             #Defines outcome if p1 plays rock and p2 plays rock
    print ("Tie")
 
elif (player1 == 'scissors' and player2 == 'paper'):        #Defines outcome if p1 plays scissors and p2 plays scissors
    print ("Player 1 snipped out Player 2.")
 
elif (player2 == 'scissors' and player2 == 'scissors'):     #Defines outcome if p1 plays scissors and p2 plays scissors
    print ("Tie")
 
elif (player1 == 'paper' and player2 == 'paper'):           #Defines outcome if p1 plays paper and p2 plays paper
    print ("Tie")
 
elif (player1 == 'paper' and player2 == 'scissors'):        #Defines outcome if p1 plays paper and p2 plays scissors
    print ("Player 2 snipped out Player 1.")
 
elif (player1 == 'rock'and player2 == 'paper'):             #Defines outcome if p1 plays Rock and p2 plays paper
    print ("Player 2 covered Player 1.")
 
elif (player1 == 'paper' and player2 == 'rock'):            #Defines outcome if p1 plays paper and p2 plays rock
    print ("Player 1 covered Player 2.")
 
elif (player1 == 'scissors' and player2 == 'rock'):         #Defines outcome if p1 plays scissors and p2 plays rock
    print ("Player 2 crushed Player 1.")
