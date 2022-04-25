#! doesnt work
import random

number = int(input('Enter your number. >>> '))
guess = random.randrange(1, 10)
correct = input(f'Was your number {guess}?')
again = input('I guessed correctly. Wanna play again? >>> ')
inagain = input('I guessed incorrectly. Wanna Play again? >>> ')

def game():
    while number != guess:
        # reassign `guess`
        guess = random.randrange(1, 10)
        if number == guess:
            correct = input(f'Was your number {guess}?')
        
if correct == 'y' or correct == 'Y':
    again = input('I guessed correctly. Wanna play again? >>> ')
elif correct == 'n' or correct == 'N':
    inagain = input('I guessed incorrectly. Wanna Play again? >>> ')

if again == 'Y' or again == 'y' or inagain == 'Y' or inagain == 'y':
    game()
else:
    pass