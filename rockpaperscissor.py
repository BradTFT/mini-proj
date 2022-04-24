import random
import time
#which game would you like to play function:

#basic idea

ask = input('Which game would you like to play? 1 or 2 >>> ')

def game1():
    actions = ['Rock', 'Paper', 'Scissor']
    ready = input('Ready to play? >>> ')
    choice = random.choice(actions)

    if ready == 'y' or 'Y':
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print(f'i chose {choice}')


#more complicated idea
def game2():
    actions = ['Rock', 'Paper', 'Scissor']
    ready = input('Ready to play? >>> ')
    chose = int(input('Chose your input: Rock(1), Paper(2), Scissor(3) >>> '))
    #computers choice
    mychoice = int(random.choice(actions))
    win = 'You Won'
    loss = 'You lost'
    tie = 'We tied'

#first issue was indentation. all of the
   if chose == 1:
        time.sleep(1)
        print('You chose Rock')
    elif chose == 2:
        time.sleep(1)
        print('You chose Paper')
    elif chose == 3:
        time.sleep(1)
        print('You chose Scissor')
    else:
        pass
        

    if ready == 'Y' or ready == 'y':
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print(f'I chose {mychoice}')
        time.sleep(1) 
        #! logic is yet to work. ill dig deeper tmr

        if mychoice == '1' and chose == 1:
            time.sleep(1)
            print(tie)
        elif mychoice == 1 and chose == 2:
            time.sleep(1)
            print(win)
        elif mychoice == 1 and chose == 3:
            time.sleep(1)
            print(loss)
        elif mychoice == 2 and chose == 1:
            time.sleep(1)
            print(loss)
        elif mychoice == 2 and chose == 2:
            time.sleep(1)
            print(tie)
        elif mychoice == 2 and chose == 3:
            time.sleep(1)
            print(win)      
        elif mychoice == 3 and chose == 1:
            time.sleep(1)
            print(win)
        elif mychoice == 3 and chose == 2:
            time.sleep(1)
            print(loss)
        elif mychoice == 3 and chose == 3:
            time.sleep(1)
            print(tie)
        else:
           pass    


    #i won or i lost
    









if ask == '1':
    game1()
elif ask == '2':
    game2()
else:
    print('invalid input')