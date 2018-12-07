from tkinter import *

def doNothing():
	print("What have I done")

root = Tk()


# ***** Main Menu *****

menu = Menu(root)
#select the menu for the root
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Project", command=doNothing)
fileMenu.add_command(label="New", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)


# ***** Toolbar *****

toolbar = Frame(root)

insert_button = Button(toolbar, text="Insert", command=doNothing)
insert_button.pack(side=LEFT, padx=2, pady=2)
print_button = Button(toolbar, text="Print", command=doNothing)
print_button.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** Status Bar *****

status = Label(root, text="Words:252", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()