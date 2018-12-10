from tkinter import *


class Screen1:

    def __init__(self, frame):
        head = Label(frame, text="Rock-Paper-Scissor", font=("",25,"bold italic"), bg="lightgrey", fg="black")
        head.pack(fill=X)



class Screen2:

    def __init__(self, frame):


class mainScreen(Screen1, Screen2):

    def __init__(self, frame):
        Screen1.__init__(self,frame)
        Screen2.__init__(self,frame)





root = Tk()

f1 = Frame(root, width=300, height=200)
# unless you fill the parent frame, you cannot fill the elements inside it
f1.pack(fill=X)

s = mainScreen(f1)

# while True:
#
#     # First, show the first screen
#
#
#     # When someone wins, show the congratulation screen.

root.mainloop()
