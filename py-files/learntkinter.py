
#!following a tutorial to learn tkinter 
#!tut is on yt by thenewboston

from tkinter import *

#root stores a blank window and builds a "base"
root = Tk() 








#runs everything
root.mainloop()




#first tutorial(labels)
'''
#add text is called a label
#parameters: 
#Root: is the blank window the label is stored in
#Text: obviously the text you want to be displayed in the window

theLabel = Label(root, text='Hello World')

#places widget
#items (buttons, text, ect are widgets)
theLabel.pack()'''

#second tutorial(buttons)

'''
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#button parameters:
#location
#value
#fg = text color bg = background color
button1 = Button(topFrame, text='Click', fg='red')
button2 = Button(topFrame, text='Click', fg='blue')
button3 = Button(topFrame, text='Click', fg='green')
button4 = Button(bottomFrame, text='Click', fg='black')


#draws items(basically widgets) to screen
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=TOP)
button4.pack()'''

#tutorial 3: fill

'''
one = Label(root, text="one", fg='white', bg='black')
two = Label(root, text="two", fg='white', bg='black')
#fill parameter: fills to the x axis and y fills to the y axis
one.pack(fill=X)
two.pack(fill=Y)
'''

#tutorial 3: grid layouts and entry(input)

'''
label1 = Label(root, text='name')
label2 = Label(root, text='password')

#entry is the same as input; adds a text field
entry1 = Entry(root)
entry2 = Entry(root)


#use grid instead of pack if specifying location
#collum is default 0
#row in 0 = top
label1.grid(row=0)
label2.grid(row=1)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
'''