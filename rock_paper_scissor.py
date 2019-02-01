from random import randint
import os

rps = ["rock", "paper", "scissor"]

while True:
    print("\n{0}Rock Paper Scissor {0}".format(('-'*8)))
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("\n4. Exit")

    while True:
        userChoice = int(input("Select one of the options(1/2/3/4): "))
        if 1 <= userChoice <= 4:
            break
        else:
            print("Invalid choice!!")

    if userChoice == 4:
        break
    compChoice = randint(1,3)

    print("You: {}".format(rps[userChoice-1]))
    print("Computer: {}\n".format(rps[compChoice-1]))

    if userChoice == compChoice :
        print("Tie")
    else:
        if ((compChoice)%3) == userChoice-1:
            print("Congratulations, YOU WON")
        else:
            print("COMPUTER WON")