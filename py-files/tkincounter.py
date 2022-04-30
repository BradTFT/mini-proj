import tkinter

#base for button. i dont understand syntax for tkin so im gonna learn that. i also dont know anything
#about adding value to the text in tkin
#but this prints to terminal every time that the button is clicked

window_main = tkinter.Tk(className='Tkinter - TutorialKart', )
window_main.geometry("400x200")
 
def submitFunction() :
    times = []
    times.append()
    print(f'Submit button has been clicked {times} times')
 
button_submit = tkinter.Button(window_main, text ="Submit", command=submitFunction)
button_submit.config(width=20, height=2)
 
button_submit.pack()
window_main.mainloop()