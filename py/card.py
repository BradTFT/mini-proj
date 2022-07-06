import random

suit = ['hearts', 'spades', 'diamonds', 'clubs']
card = ['Joker', 'Jack','Queen', 'King', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


randsuit = random.sample(suit,1)
randcard = random.sample(card,1)


output = print(f'Your card is the {randcard} for {randsuit}')
#super lazy bc it prints with the brackets but idrc im trying to retain my sanity