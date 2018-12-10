from tkinter import *

equa = ""
data = ""
def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def operPress(op):
    global equa
    if len(equa) != 0:
        btnPress(op)
    else:
        equa = data + str(op)
        equation.set(equa)

def evaluate():
    global equa
    global data
    data = str(eval(equa))
    equation.set(equa + " = " + data)
    equa = ""

def clear():
    global equa
    equa=""
    equation.set(equa)

master = Tk()

root = Frame(master, padx=20, pady=10, bg="white")
root.grid()

# Equation label
equation = StringVar()
calculation = Label(root, textvariable=equation,  bg="white")
equation.set("")
calculation.grid(columnspan=4, sticky=E)

button1 = Button(root, text="1", command=lambda: btnPress(1), font=("",18))
button1.grid(row=1, column=0)
button2 = Button(root, text="2", command=lambda: btnPress(2), font=("",18))
button2.grid(row=1, column=1)
button3 = Button(root, text="3", command=lambda: btnPress(3), font=("",18))
button3.grid(row=1, column=2)
button4 = Button(root, text="4", command=lambda: btnPress(4), font=("",18))
button4.grid(row=2, column=0)
button5 = Button(root, text="5", command=lambda: btnPress(5), font=("",18))
button5.grid(row=2, column=1)
button6 = Button(root, text="6", command=lambda: btnPress(6), font=("",18))
button6.grid(row=2, column=2)
button7 = Button(root, text="7", command=lambda: btnPress(7), font=("",18))
button7.grid(row=3, column=0)
button8 = Button(root, text="8", command=lambda: btnPress(8), font=("",18))
button8.grid(row=3, column=1)
button9 = Button(root, text="9", command=lambda: btnPress(9), font=("",18))
button9.grid(row=3, column=2)
button0 = Button(root, text="0", command=lambda: btnPress(0), font=("",18))
button0.grid(row=4, column=1)

minus = Button(root, text="-", command=lambda: operPress("-"), font=("",18))
minus.grid(row=1, column=3)
plus = Button(root, text="+", command=lambda: operPress("+"), font=("",16))
plus.grid(row=2, column=3)
multiply = Button(root, text="*", command=lambda: operPress("*"), font=("",18))
multiply.grid(row=3, column=3)
divide = Button(root, text="/", command=lambda: operPress("/"), font=("",18))
divide.grid(row=4, column=3)
equals = Button(root, text="=", command=evaluate, font=("",18))
equals.grid(row=4, column=2)
clear = Button(root, text="C", command=clear, font=("",18))
clear.grid(row=4, column=0)

master.mainloop()