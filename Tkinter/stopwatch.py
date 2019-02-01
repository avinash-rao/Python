from tkinter import *

running = False
counter = -1

def counter_label(label):
    def count():
        if running:
            global counter
            if counter == -1:
                display = "Starting..."
            else:
                display = str(counter)

            label['text'] = display
            label.after(1000, count)
            counter += 1
    count()

def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    reset['state'] = 'normal'
    stop['state'] = 'normal'

def Stop():
    global running
    running = False
    start['state'] = 'normal'
    reset['state'] = 'normal'
    stop['state'] = 'disabled'

def Reset(label):
    global counter
    counter = -1
    if running == False:
        label['text'] = "Welcome"
        start['state'] = 'normal'
        reset['state'] = 'disabled'
        stop['state'] = 'disabled'
    else:
        label['text'] = "Starting..."

root = Tk()
root.title("Stopwatch")
root.minsize(width=250, height=70)

label = Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()

start = Button(root, text='Start', width=15, command=lambda:Start(label))
stop = Button(root, text='Stop', width=15, state='disabled', command=Stop)
reset = Button(root, text='Reset', width=15, state='disabled', command=lambda:Reset(label))
start.pack()
stop.pack()
reset.pack()
root.mainloop()