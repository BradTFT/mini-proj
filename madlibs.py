#! work in progress

import random

first = input()
second = input()
third = input()
fourth = input()
fifth = input()
sixth = input()
seventh = input()

do_you_know = input('If you know how MadLibs works, enter(y). If not, enter(n). >>> ')


#i want multiple different stories. so each will be its own function and the random module will chose one


#inital game function
def game():
    pass
    


#different games functions(these are the different varaitions of each game)
def game1():
    pass


def game2():
    pass


def game3():
    pass


def game4():
    pass


def game5():
    pass



if do_you_know == 'y' or do_you_know == 'Y':
    game()
elif do_you_know == 'n' or do_you_know == 'Y':
    print('To play MadLibs, follow the instructions and pick a word that fulfuls the catagory stated. at the end of the game, you will have a story with the words you chose')
else: 
    pass