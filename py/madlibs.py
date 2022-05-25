import random
#idea is that the functions are going to ask for input for each replacable word and then stitch it together and print the result
#games
#color libs
import colorama
from colorama import Fore, Back, Style
#init function
colorama.init(autoreset=True)
#resets color inside of {} f string
foreReset = Fore.RESET
backReset = Back.RESET

def game1():
    one = input('Noun >>> ')
    two = input('Adverb >>> ')
    three = input('Adverb >>> ')
    four = input('Noun >>> ')
    five = input('Adverb >>> ')
    six = input('Clothing item >>> ')
    seven = input('Adverb >>> ')
    eight = input('Adverb >>> ')
    nine = input('Adverb >>> ')
    ten = input('number >>> ')
    eleven = input('adjective >>> ')
    twelve = input('verb >>> ')
    thirteen = input('noun >>> ')
    fourteen = input('noun >>> ')
    fifteen = input('noun >>> ')
    sixteen = input('adjective >>> ')
    seventeen = input('adjective >>> ')
    eigheten = input('noun >>> ')
    ninetten = input('adj >>> ')
    twenty = input('noun >>> ')
    twentyOne = input('noun >>> ')
    one_colored = Fore.RED + one
    two_colored = Fore.RED + two
    three_colored = Fore.RED + three
    four_colored = Fore.RED + four
    five_colored = Fore.RED + five
    six_colored = Fore.RED + six
    seven_colored = Fore.RED + seven
    eight_colored = Fore.RED + eight
    nine_colored = Fore.RED + nine
    ten_colored = Fore.RED + ten
    eleven_colored = Fore.RED + eleven
    twelve_colored = Fore.RED + twelve
    thirteen_colored = Fore.RED + thirteen
    fourteen_colored = Fore.RED + fourteen
    fifteen_colored = Fore.RED + fifteen
    sixteen_colored = Fore.RED + sixteen
    seventeen_colored = Fore.RED + seventeen
    eigheten_colored = Fore.RED + eigheten
    ninetten_colored = Fore.RED + ninetten
    twenty_colored = Fore.RED + twenty
    twentyOne_colored = Fore.RED + twentyOne
    print(f'''
    Lets build a snowman,” said {one_colored}{foreReset}. First we need to have a {two_colored}{foreReset} snowstorm.
    As we watched the snow fall {three_colored}{foreReset} from the sky it made me so hungry that I could eat {four_colored}{foreReset}.
    Once there was enough snow, we went outside to build the {five_colored}{foreReset} snowman ever. 
    We grabbed our {six_colored}{foreReset} that was {seven_colored}{foreReset} and {eight_colored}{foreReset}.
    We began rolling the snow {nine_colored}{foreReset} until we couldn’t lift it anymore. We did this again and again until there were {ten_colored}{foreReset} {eleven_colored}{foreReset} on top of each other. 
    We {twelve_colored}{foreReset} to find {thirteen_colored}{foreReset} in the road,
    but could only find {fourteen_colored}{foreReset}. The eyes were made of {fifteen_colored}{foreReset}, the nose was a {sixteen_colored} {seventeen_colored} {eigheten_colored}.
    {foreReset}Mom gave us her old {ninetten_colored}{foreReset} to use for the top of his head. We stepped back and said this is the {twenty_colored}{foreReset} snowman we have ever made and we called him {twentyOne_colored}{foreReset}.''')
#working i just messed my numbers up
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


#game chooser
getGame = random.randrange(1, 6)


if getGame == 1:
    game1()
elif getGame == 2:
    game2()
elif getGame == 3:
    game3()
elif getGame == 4:
    game4()
elif getGame == 5:
    game5()
elif getGame == 6:
    game6()
