from tkinter import *

root = Tk()

def printName():
	print('Hello, Avi!')

button1 = Button(root, text="Print my name", command=printName)
button1.pack()

root.mainloop()