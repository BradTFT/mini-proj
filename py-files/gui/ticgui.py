from tkinter import *
import tkinter as tk
from tkinter.tix import COLUMN
#! basic click detection is all set. Just need to position everything to a grid.
#! i think i have to make a seperate funct for every button. shouldnt be an issue.
#* ^^^ there is prob a better way to do it but its fine it works and thats all that matters.
#!works
root = Tk()

def lclick1(event):
    button1.config(text='X')
    print('this button is now X')


def rclick1(event):
    button1.config(text='O')
    print('this button is now O')

def lclick2(event):
    button2.config(text='X')
    print('this button is now X')


def rclick2(event):
    button2.config(text='O')
    print('this button is now O')

def lclick3(event):
    button3.config(text='X')
    print('this button is now X')


def rclick3(event):
    button3.config(text='O')
    print('this button is now O')

def lclick4(event):
    button4.config(text='X')
    print('this button is now X')


def rclick4(event):
    button4.config(text='O')
    print('this button is now O')

def lclick5(event):
    button5.config(text='X')
    print('this button is now X')


def rclick5(event):
    button5.config(text='O')
    print('this button is now O')

def lclick6(event):
    button6.config(text='X')
    print('this button is now X')


def rclick6(event):
    button6.config(text='O')
    print('this button is now O')

def lclick7(event):
    button7.config(text='X')
    print('this button is now X')


def rclick7(event):
    button7.config(text='O')
    print('this button is now O')


def lclick8(event):
    button8.config(text='X')
    print('this button is now X')


def rclick8(event):
    button8.config(text='O')
    print('this button is now O')

def lclick9(event):
    button9.config(text='X')
    print('this button is now X')


def rclick9(event):
    button9.config(text='O')
    print('this button is now O')

def reset(event):
    button1.config(text='')
    button2.config(text='')
    button3.config(text='')
    button4.config(text='')
    button5.config(text='')
    button6.config(text='')
    button7.config(text='')
    button8.config(text='')
    button9.config(text='')

button1 = Button(root)
button2 = Button(root)
button3 = Button(root)
button4 = Button(root)
button5 = Button(root)
button6 = Button(root)
button7 = Button(root)
button8 = Button(root)
button9 = Button(root)
resetbutton = Button(root, text="RESET")

resetbutton.bind('<Button-1>', reset)

button1.bind('<Button-1>', lclick1)
button1.bind('<Button-3>', rclick1)

button2.bind('<Button-1>', lclick2)
button2.bind('<Button-3>', rclick2)

button3.bind('<Button-1>', lclick3)
button3.bind('<Button-3>', rclick3)

button4.bind('<Button-1>', lclick4)
button4.bind('<Button-3>', rclick4)

button5.bind('<Button-1>', lclick5)
button5.bind('<Button-3>', rclick5)

button6.bind('<Button-1>', lclick6)
button6.bind('<Button-3>', rclick6)

button7.bind('<Button-1>', lclick7)
button7.bind('<Button-3>', rclick7)

button8.bind('<Button-1>', lclick8)
button8.bind('<Button-3>', rclick8)

button9.bind('<Button-1>', lclick9)
button9.bind('<Button-3>', rclick9)





button1.grid(row=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
resetbutton.grid(row=3, column=1)
root.mainloop()