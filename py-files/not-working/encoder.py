


#! so i kind of fixed it. just needs to be refined


from dataclasses import replace

typeof = int(input('Encode a message(1) or Decode a message(2) >>> '))

if typeof == 1:
    message = str(input("Message Here: >>> "))
    new_string = message.replace('a', 'b').replace('c', 'd').replace('e', 'f')
    print(f'Old message:\n{message}\nNew message: \n{new_string}')

if typeof == 2:
    message = str(input("Message Here: >>> "))
    new_string = message.replace('f', 'e').replace('d', 'c').replace('b', 'a')
    print(f'The message says \n{new_string}')
