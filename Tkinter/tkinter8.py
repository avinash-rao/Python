from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Fact', 'All is Well')

answer = tkinter.messagebox.askquestion('Question', 'Do you like funny face')

if answer == 'yes':
    print(' 8===D~ ')

root.mainloop()