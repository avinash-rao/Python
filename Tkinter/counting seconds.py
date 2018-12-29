from tkinter import *

counter = 0

def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()

root = Tk()
root.geometry("200x100")
root.title("Counting Seconds")
label = Label(root, fg="green", font=("", 20))
label.pack(expand=True)
counter_label(label)
button = Button(root, text="Stop", width=25, command=root.quit)
button.pack(side=BOTTOM, fill=X)

root.mainloop()