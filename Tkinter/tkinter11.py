from tkinter import *

root = Tk()

def evaluate(event):
    data = e.get()
    ans.configure(text="Answer: " + str(eval(data)))

root.geometry("200x100")

title = Label(root, text="Enter your expression: ", font=("Times",12,"bold italic"))
title.pack()
e = Entry(root)
e.bind("<Return>", evaluate)
e.pack()

ans = Label(root)
ans.pack(side=LEFT)

root.mainloop()