from tkinter import *
from random import randint

global rps
rps = ["rock", "paper", "scissor"]
global compChoice
global userChoice
userChoice = 0
compChoice = None

def Rock(label):
    global userChoice
    global compChoice
    userChoice = 1
    compChoice = randint(1, 3)
    display(label)

def Paper(label):
    global userChoice
    global compChoice
    userChoice = 2
    compChoice = randint(1, 3)
    display(label)

def Scissor(label):
    global userChoice
    global compChoice
    userChoice = 3
    compChoice = randint(1, 3)
    display(label)


def display(label):
    global userChoice
    global compChoice
    global rps
    str = "You: " + rps[userChoice-1] + "\nComputer: " + rps[compChoice-1] + '\n\n'
    label['text'] = str
    if userChoice == compChoice:
        label['text'] = '\n\n'.join([str, "Tie"])
    else:
        if ((compChoice) % 3) == userChoice - 1:
            label['text'] = '\n\n'.join([str, "Congratulations, YOU WON"])
        else:
            label['text'] = '\n\n'.join([str, "COMPUTER WON"])

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