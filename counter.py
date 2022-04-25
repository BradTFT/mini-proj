#! doesnt work


input = input('>>> ')
count = [0]


def add():
    count.append(1)
    print(count)
    

def remove():
    count.remove(1)
    print(count)



for x in count:
    if input == "+":
        add()
        continue
        
        

    elif input == '-':
        remove()
        continue
        





        
        


