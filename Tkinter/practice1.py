from tkinter import *

class screen1:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        label = Label(frame, text="Screen 1")
        label.pack()

        self.button1 = Button(frame, text="Go to screen 2", command= lambda: self.switch_frame(master, frame))
        self.button1.pack()

    def switch_frame(self, master, frame):
        frame.destroy()
        ob = screen2(master)

class screen2:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        label = Label(frame, text="Screen 2")
        label.pack()


root = Tk()

f = screen1(root)
# f = screen2(root)

root.mainloop()