import time
import math
import random

gameOn = True
print("Let's Play Paper Scissors Rock")


while gameOn:
    player = False
    player = input("Press p for paper, s for scissors, r for rock, q for quit\n")
    if player == "q":
        gameOn = False
    else:
        if player == "r":
            print("rock")
            comp = random.randint(1,3)
        elif player == "p":
            print("paper")
            comp = random.randint(1,3)
        elif player == "s":
            print("scissors")
            comp = random.randint(1,3)
        else:
            print("Error: Invalid input")
            comp = False
        if comp == 1:
            print("rock")
        if comp == 2:
            print("paper")
        if comp == 3:
            print("scissors")
        if player == "r":
            if comp == 3:
                print("You Won!")
            elif comp == 2:
                print("You Lost:(")
            else:
                print("A Draw!")
        if player == "p":
            if comp == 1:
                print("You Won!")
            elif comp == 3:
                print("You Lost:(")
            else:
                print("A Draw!")
        if player == "s":
            if comp == 2:
                print("You Won!")
            elif comp == 1:
                print("You Lost:(")
            else:
                print("A Draw!")

print("Bye, Hope I see you soon")