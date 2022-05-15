from tkinter import *
import tkinter as tk
#! basic click detection is all set. Just need to position everything to a grid.
root = Tk()

def lclick(event):
    buttontest.set('X')
    print('this button is now X')


def rclick(event):
    buttontest.set('O')
    print('this button is now O')



buttontest = Button(root, text='')

buttontest.bind('<Button-1>', lclick)
buttontest.bind('<Button-3>', rclick)

buttontest.pack()


root.mainloop()