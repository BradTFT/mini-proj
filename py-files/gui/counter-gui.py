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
enter = Button(root, text='Show total')
clear = Button(root, text='Clear')

one.bind('<Button-1>', addone)
two.bind('<Button-1>', addtwo)
three.bind('<Button-1>', addthree)
enter.bind('<Button-1>', entered)
clear.bind('<Button-1>', cleared)

one.pack()
two.pack()
three.pack()
enter.pack()
clear.pack()



root.mainloop()