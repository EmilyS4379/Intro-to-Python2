from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
 
while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer: 
        print("try again")
    elif player == "Rock":
        if computer == "Paper":
            print("you lose! paper covers rock")
        if computer == "Scissors":
            print ("you win, rock smashes scissors")
    elif player == "Paper":
        if computer == "Paper":
            print("try again")
        if computer == "Rock":
            print("You win! paper covers rock")
        if computer == "Scissors":
            print("you lose, scissors cuts paper")
    elif player == "Scissors":
        if computer == "Scissors":
            print("try again")
        if computer == "Paper":
            print("you win! scissors cuts paper")
        if computer == "Rock":
            print("you lose! rock crushes scissors")
    