from tkinter import *

root = Tk()

#notice the argument-'event'
def printName(event):
	print("Hello, my name is Avi")

button1 = Button(root, text="Print my name")
button1.bind("<Button-1>", printName)
button1.pack()

root.mainloop()