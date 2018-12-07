from tkinter import *

root = Tk()

photo = PhotoImage(file=r"Headphones_ONN1.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()