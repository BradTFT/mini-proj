import random
#! work in progress (pain in the ass)
howto = print('''How to play:
Enter the number on the grid of where you want to place your mark
Computer is "O" and Player is "X"''')

ready = input('Ready to play? >>> ')
grid = '''
      |     |     
   1  |  2  |  3  
 _____|_____|_____
      |     |     
   4  |  5  |  6  
 _____|_____|_____
      |     |     
   7  |  8  |  9  
      |     |     '''

first = input('Enter the number of the slot you wish to take. >>> ')

if first == '1':
    print('''
      |     |     
   X  |  2  |  3  
 _____|_____|_____
      |     |     
   4  |  5  |  6  
 _____|_____|_____
      |     |     
   7  |  8  |  9  
      |     |     ''')
elif first == '2':
    print('''
      |     |     
   1  |  X  |  3  
 _____|_____|_____
      |     |     
   4  |  5  |  6  
 _____|_____|_____
      |     |     
   7  |  8  |  9  
      |     |     ''')
elif first == '3':
    print('''
      |     |     
   1  |  2  |  X  
 _____|_____|_____
      |     |     
   4  |  5  |  6  
 _____|_____|_____
      |     |     
   7  |  8  |  9  
      |     |     ''')
elif first == '4':
    print('''
      |     |     
   1  |  2  |  3  
 _____|_____|_____
      |     |     
   X  |  5  |  6  
 _____|_____|_____
      |     |     
   7  |  8  |  9  
      |     |     ''')
elif first == '5':
    print('''
      |     |     
   1  |  2  |  3  
 _____|_____|_____
      |     |     
   4  |  X  |  6  
 _____|_____|_____
      |     |     
   7  |  8  |  9  
      |     |     ''')
elif first == '6':
    print('''
      |     |     
   1  |  2  |  3  
 _____|_____|_____
      |     |     
   4  |  5  |  X  
 _____|_____|_____
      |     |     
   7  |  8  |  9  
      |     |     ''')
elif first == '7':
    print('''
      |     |     
   1  |  2  |  3  
 _____|_____|_____
      |     |     
   4  |  5  |  6  
 _____|_____|_____
      |     |     
   X  |  8  |  9  
      |     |     ''')
elif first == '8':
    print('''
      |     |     
   1  |  2  |  3  
 _____|_____|_____
      |     |     
   4  |  5  |  6  
 _____|_____|_____
      |     |     
   7  |  X  |  9  
      |     |     ''')
elif first == '9':
    print('''
      |     |     
   1  |  2  |  3  
 _____|_____|_____
      |     |     
   4  |  5  |  6  
 _____|_____|_____
      |     |     
   7  |  8  |  X  
      |     |     ''')
else:
    pass









if ready == 'n' or ready == 'N':
    pass

