import random

#ok so this generator is gonna have the user specify the things it needs


lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
numbers = '1234567890'
spec_characters = '!@#$%^&*()-_?.,'

x = int(input('How many characters would you like your password to be? >>> '))

string = lower + upper + numbers + spec_characters
length = x 
password = "".join(random.sample(string, length))

print(f'Your password is: {password}')
