
#!all thats next is figuring out how to get this into a box and out of the terminal
from tkinter import *
root = Tk()

numbers = []
total0 = 0

def addone(event):
    print('1 was added')
    numbers.append(1)

def addtwo(event):
    print('2 was added')
    numbers.append(2)

def addthree(event):
    print('3 was added')
    numbers.append(3)

def addfour(event):
    print('4 was added')
    numbers.append(4)

def addfive(event):
    print('5 was added')
    numbers.append(5)

def addsix(event):
    print('6 was added')
    numbers.append(6)

def addseven(event):
    print('7 was added')
    numbers.append(7)

def addeight(event):
    print('8 was added')
    numbers.append(8)

def addnine(event):
    print('9 was added')
    numbers.append(9)

def addten(event):
    print('10 was added')
    numbers.append(10)

#! add code to make this work. only works with "1"s. need to subtract one
#!instead of removing it
def remove1(event):
    print('removed 1 from total')
    numbers.remove(1)

def entered(event):
    print(sum(numbers))

#* fix this: make it so it adds the numbers in the list (numbers) 
# and prints the value of the counted numbers as the final number

#! solved =>
#changed all numerical function values to integers instead of strings.


def cleared(event):
    numbers.clear()

one = Button(root, text='1')
two = Button(root, text='2')
three = Button(root, text='3')
four = Button(root, text='4')
five = Button(root, text='5')
six = Button(root, text='6')
seven = Button(root, text='7')
eight = Button(root, text='8')
nine = Button(root, text='9')
ten = Button(root, text='10')
removeone = Button(root, text='-1')
enter = Button(root, text='Show total')
clear = Button(root, text='Clear')

one.bind('<Button-1>', addone)
two.bind('<Button-1>', addtwo)
three.bind('<Button-1>', addthree)
four.bind('<Button-1>', addfour)
five.bind('<Button-1>', addfive)
six.bind('<Button-1>', addsix)
seven.bind('<Button-1>', addseven)
eight.bind('<Button-1>', addeight)
nine.bind('<Button-1>', addnine)
ten.bind('<Button-1>', addten)
removeone.bind('<Button-1>', remove1)

enter.bind('<Button-1>', entered)
clear.bind('<Button-1>', cleared)


one.pack()
two.pack()
three.pack()
four.pack()
five.pack()
six.pack()
seven.pack()
eight.pack()
nine.pack()
ten.pack()
removeone.pack()
enter.pack()
clear.pack()



root.mainloop()