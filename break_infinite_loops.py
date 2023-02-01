while True:
  print('I love you!')
  break


import time
counter = 0

while counter <= 10:
    counter+=1

    print(counter)
    time.sleep(1)

import random
while True:
 
    random_number = random.randrange(1000)
    print(random_number)
 
    if random_number == 777:
        print('Found!')
        break



names = ['Max', 'Felix', 'Deniz', 'Selin', 'Lucas', 26, 'Sarah']
 
for name in names:
 
    if type(name) != str:
        print('Found', name)
        break
 
    else:
        print(name, 'is a string!')