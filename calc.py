import random

floatorint = input('Does your calculations require whole numbers(1) or decimals(2)? >>> ')

def inte():
    firstint = int(input('>>>'))
    opint = input('>>>')
    secondint = int(input('>>>'))


    if opint == 'x' or opint == 'X' or opint == '*':
        print(firstint * secondint)
    elif opint == '-':
        print(firstint - secondint)
    elif opint == '+':
        print(firstint + secondint)
    elif opint == '/':
        print(firstint / secondint)


def floate():
    firstfloat = float(input('>>>'))
    opfloat = input('>>>')
    secondfloat = float(input('>>>'))


    if opfloat == 'x' or opfloat == 'X' or opfloat == '*' :
        print(firstfloat * secondfloat)
    elif opfloat == '-':
        print(firstfloat - secondfloat)
    elif opfloat == '+':
        print(firstfloat + secondfloat)
    elif opfloat == '/':
        print(firstfloat / secondfloat)


if floatorint == '2':
    floate()
elif floatorint == '1':
    inte()
else:
    pass
