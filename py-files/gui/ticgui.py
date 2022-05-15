from tkinter import *
import tkinter as tk
#! basic click detection is all set. Just need to position everything to a grid.
#! cant figure out how to change the button text onClick
root = Tk()

def lclick(event):
    print('this button is now X')


def rclick(event):
    print('this button is now O')


buttontest = Button(root)

buttontest.bind('<Button-1>', lclick)
buttontest.bind('<Button-3>', rclick)

buttontest.pack()


root.mainloop()