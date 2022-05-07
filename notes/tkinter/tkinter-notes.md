# learning tkinter these are my notes from following (thenewboston) on youtube tutorials




## first tutorial(labels)
```
#add text is called a label
#parameters: 
#Root: is the blank window the label is stored in
#Text: obviously the text you want to be displayed in the window

theLabel = Label(root, text='Hello World')

#places widget
#items (buttons, text, ect are widgets)
theLabel.pack()
```

## tutorial 2: buttons

```
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
button4.pack()
```

## tutorial 3: fill

```
one = Label(root, text="one", fg='white', bg='black')
two = Label(root, text="two", fg='white', bg='black')
#fill parameter: fills to the x axis and y fills to the y axis
one.pack(fill=X)
two.pack(fill=Y)
```


## tutorial 4: grid layouts and entry(input)


```
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

#sticky parameter:
#N orth E ast S outh W est
```

## tutorial 5: more on grids

```
c = Checkbutton(root, text='Keep me logged in')

#spans across 2 columns based off of parameter
c.grid(columnspan=2)
```


## tutorial 6: function binding to widgets



```#event param is alternate method
def printName(event):
    print('Hello World')

button1 = Button(root, text="Clicketh me")
#event is tied to bind funct


button1.bind("<Button-1>", printName)
button1.pack()


#command paramter tells button to run function when clicked
button1 = Button(root, text="Clicketh me", command=printName)

button1.pack()
```


## tutorial 7: mouse click events.


```

def leftClick(event):
    print('left')


def rightClick(event):
    print('right')

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind('<Button-3>', rightClick)
frame.pack()
```

## tutorial 8: classes with tkinter

```
#classes in tkinter must contain the parameter master next to self
#master takes the place of root in the class
class Buttons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text='Printed message', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='Quit', command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('i doubted you but this works')

#calls all items in the class with one line
b = Buttons(root)
```

## tutorial 9: dropdown menus


