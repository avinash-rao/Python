from tkinter import *

class Screen:

    playerScore = 0
    computerScore = 0
    def __init__(self, master):
        frame = Frame(master)
        frame.pack(fill=X)

        self.head = Label(frame, text="Rock Paper Scissor", font=("",25,"bold italic"), bg="lightgrey")
        self.head.pack(fill=X, side=TOP)

        self.screenTwo(frame)


    def screenOne(self, frame):

        label1 = Label(frame, text="Select any one: ", font=("Times",18,"italic"))
        label1.pack(side=TOP, anchor=W)

        RPSframe = Frame(frame, width=300, height=100)
        RPSframe.pack()

        rock = Button(RPSframe, text="Rock", bg="white", font=("",14))
        rock.pack(side=LEFT, padx=4, pady=4)
        paper = Button(RPSframe, text="Paper", bg="white", font=("",14))
        paper.pack(side=LEFT, padx=4, pady=4)
        scissor = Button(RPSframe, text="Scissor", bg="white", font=("",14))
        scissor.pack(side=LEFT, padx=4, pady=4)


        status = Frame(frame,pady=10, bd=1)
        status.pack(side=BOTTOM, fill=X)
        cScore = Label(status, text=f"Computer's Score: {self.computerScore}", relief=SUNKEN, anchor=W)
        cScore.pack(anchor=W, side=BOTTOM, fill=X)
        mScore = Label(status, text=f"Your Score: {self.playerScore}", relief=SUNKEN, anchor=W)
        mScore.pack(anchor=W, side=BOTTOM, fill=X)

    def screenTwo(self, frame):

        # "Congratulations" or "Better luck next time" (depending on who wins)

        # Would you like to play again?
        ask = Label(frame, text="Would you like to play again?",  font=("Times",18,"italic"))
        ask.pack(side=LEFT)

        yes = Button(frame, text="yes")
        yes.pack(side=LEFT)
        no = Button(frame, text="no")
        no.pack(side=LEFT)




root = Tk()

ob = Screen(root)


root.mainloop()