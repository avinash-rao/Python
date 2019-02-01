from tkinter import *
from random import randint

global rps
rps = ["rock", "paper", "scissor"]
global compChoice
global userChoice
userChoice = 0
compChoice = randint(1,3)

def Rock(label):
    global userChoice
    userChoice = 1
    display(label)

def Paper(label):
    global userChoice
    userChoice = 2
    display(label)

def Scissor(label):
    global userChoice
    userChoice = 3
    display(label)


def display(label):
    global userChoice
    global compChoice
    global rps
    str = "You: " + rps[userChoice-1] + "\nComputer: " + rps[compChoice-1]
    label['text'] = str
    if userChoice == compChoice:
        label['text'] = '\n\n'.join([str, "Game Draw"])

    elif userChoice!=2 and compChoice!=2:           # When the user and comp chooses first and last element of list
        if userChoice%3 > compChoice%3 :
            label['text'] = '\n\n'.join([str, "User Won"])
        else:
            label['text'] = '\n\n'.join([str, "Computer Won"])

    else:                                           # When the choices are consecutive
        if userChoice > compChoice :
            label['text'] = '\n\n'.join([str, "User Won"])
        else:
            label['text'] = '\n\n'.join([str, "Computer Won"])

root = Tk()
root.title("Rock Paper Scissor")
# root.minsize(width=750, height=250)
rock = Button(root, text="Rock", command=lambda:Rock(label))
paper = Button(root, text="Paper", command=lambda:Paper(label))
scissor = Button(root, text="Scissor", command=lambda:Scissor(label))
rock.pack(side=LEFT)
paper.pack(side=LEFT)
scissor.pack(side=LEFT)

label = Label(root)
label.pack(side=BOTTOM)

root.mainloop()