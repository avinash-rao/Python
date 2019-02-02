from tkinter import *
from random import randint

global rps
rps = ["rock", "paper", "scissor"]
global compChoice
global userChoice
userChoice = None
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
    str = "You: " + rps[userChoice-1] + "\n\nComputer: " + rps[compChoice-1] + '\n\n'
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
root.minsize(width=300, height=250)

# write frame1 and frame2 here
frame1 = Frame(root, padx=5, pady=5)
frame2 = Frame(root, padx=5, pady=5)
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)

rock = Button(frame1, text="Rock", command=lambda:Rock(label), padx=30, pady=20)
paper = Button(frame1, text="Paper", command=lambda:Paper(label), padx=30, pady=20)
scissor = Button(frame1, text="Scissor", command=lambda:Scissor(label), padx=30, pady=20)
rock.pack(side=LEFT)
paper.pack(side=LEFT)
scissor.pack(side=LEFT)

label = Label(frame2)
label.pack(side=BOTTOM)

root.mainloop()