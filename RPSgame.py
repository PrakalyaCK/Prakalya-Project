print("--------ROCK PAPER SCISSORS---------")
print('''         LET'S START              ''')

from random import randint


t = ["rock", "paper", "scissors"]


computer = t[randint(0,2)]


player = "yes"

while player == "yes":

    player = input("Rock, Paper, Scissors:")
    if player == computer:
        print("Tie!")
    elif player.lower() == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player.lower() == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player.lower() == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    player=input("want to play again(yes/no):")
    
    
    computer = t[randint(0,2)]
