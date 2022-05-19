
#! WORKS AS A CALCULATOR
from tkinter import *
root = Tk()

numbers = []

def addone(event):
    numbers.append('1')

def addadd(event):
    numbers.append('+')

def splice(event):
    first = int(numbers[0])
    second = int(numbers[2])
    print(first + second)

def cleared(event):
    numbers.clear()

def show(event):
    print(numbers)
    
one = Button(root, text='1')
add1 = Button(root, text='+')
equals = Button(root, text='=')
clear = Button(root, text='Clear tracked')
test = Label(root, text='show')

one.bind('<Button-1>', addone)
add1.bind('<Button-1>', addadd)
equals.bind('<Button-1>', splice)
clear.bind('<Button-1>', cleared)
test.bind('<Button-1>', show)


one.pack()
add1.pack()
equals.pack()
clear.pack()
test.pack()

root.mainloop()