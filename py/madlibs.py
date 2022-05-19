#! work in progress

import random

#!attempting to fix

start = input('Press ENTER to start')

#entries:
'''
first = input()
second = input()
third = input()
fourth = input()
fifth = input()
sixth = input()
seventh = input()
'''
#i want multiple different stories. so each will be its own function and the random module will chose one



    


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

def game6():
    pass

#!trying to chose a random function but its calling all of them instead
games_list = [game1(), game2(), game3(), game4(), game5(), game6()]

random.choice(games_list)
