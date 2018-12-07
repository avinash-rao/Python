from tkinter import *


class aviButtons:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		# When calling the same class function, don't forget to include 'self' with '.' operator
		self.printButton = Button(frame, text="Print Message", command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)

	def printMessage(self):
		print("This works!")

root = Tk()
ob = aviButtons(root)
root.mainloop()