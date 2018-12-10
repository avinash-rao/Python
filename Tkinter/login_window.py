from tkinter import *

root = Tk()

title = Label(root, text="Login Page", font=("", 14, "bold"))
title.grid(columnspan=2)

# Name
nameLabel = Label(root, text="Name")
nameLabel.grid(row=1, column=0, sticky=E)

nameEntry = Entry(root)
nameEntry.grid(row=1, column=1)

# Password
psdLabel = Label(root, text="Password")
psdLabel.grid(row=2, column=0, sticky=E)

psdEntry = Entry(root)
psdEntry.grid(row=2, column=1)


# Keep me signed in
c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()