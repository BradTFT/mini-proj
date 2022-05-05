#! sucks doesnt work


#!i have a new idea for this but im running into a problem with the string = replace + replace where
#! its printing the replaced and the copy of the original.


input = str(input("Message Here: >>> "))

def replaceString():
    input.replace('a', 'b')
    input.replace('b',  'c')

string = replaceString()

print(string)