import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
numbers = input()
numbers_colored = Fore.RED + numbers 
afterReset = Fore.RESET

print(f'this is a test to find {numbers_colored} {afterReset}if this works  ')