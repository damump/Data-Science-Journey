#Make a two-player Rock-Paper-Scissors game.
#(Hint: Ask for player plays (using input), compare them, print out a message
# of congratulations to the winner, and ask if the players want to start a new
 #game

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

player1 = input("paper rock or scissors ").lower()
options = ["paper","rock","scissors"]
player2 = random.choice(options)

if player1 == player2:
    print("It's a tie! ")
elif player1 = "paper" & player2 = "rock":
    print("Paper wins!")
    else:
        print("Scissors wins!")
elif player1 = "rock" & player2 = "scissors"
