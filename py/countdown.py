import time

gettime = int(input('enter countdown time >>> '))
print(gettime)
while gettime != 0:
    gettime = gettime - 1
    time.sleep(1)
    print(gettime)

#! add sound here: