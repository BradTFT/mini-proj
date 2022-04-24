
import random

number = input('Enter your number. >>> ')

guess = random.randrange(1, 10)

while number != guess:
    # reassign `guess`
    guess = random.randrange(1, 10)
    print(guess)

if number == guess:
    print(f'Was your number {guess}')