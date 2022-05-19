from random_word import RandomWords
r = RandomWords()
word = r.get_random_word()
x = []
difficulty = int(input('Select Difficulty \n(1)Easy(3-5 letters) \n(2)Medium(5-8 letters) \n(3)Hard(8-12 letters)\n'))

#! ok so i think i need to make a class so it constantly loops thru. i have the basics done
#! it takes a word from the dictionary and prints the length of the word based on the entered difficulty
#! all i need is the interaction part

if difficulty == 1:
    easyword = r.get_random_word(minLength=3, maxLength=5)
    print(len(easyword))




'''
for i in x:
    if difficulty == 1:
        easyword = r.get_random_word(minLength=3, maxLength=5)
        print(f'The word is {easyword}')
    elif difficulty == 2:
        medword = r.get_random_word(minLength=5, maxLength=8)
        print(f'The word is {medword}')
    elif difficulty == 3:
        hardword = r.get_random_word(minLength=8, maxLength=12)
        print(f'The word is {hardword}')
'''



