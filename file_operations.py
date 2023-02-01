message_file = open("message.txt") #default read mode
content = message_file.read()
message_file.close()
print(content)

hello_file = open("hello.txt","a") #w is overwrite mode, a is append mode
hello_file.write(" World")
hello_file.close()

import random
while True:

  random_number = random.randrange(1000)
  print(random_number)
 
  if random_number == 777:
    print('Found!')
    break



numbers_file = open('number_history.txt', 'w')
 
while True:
 
  random_number = random.randrange(1000)
  print(random_number)
  numbers_file.write(str(random_number))
  numbers_file.write('\n')
 
  if random_number == 777:
    print('Found!')
    numbers_file.write('Found!')
    numbers_file.close()
    break




import random
 
with open('number_history2.txt', 'w') as numbers_file:
 
  while True:

    random_number = random.randrange(1000)
    print(random_number)
    numbers_file.write(str(random_number))
    numbers_file.write('\n')
 
    if random_number == 777:
      print('Found!')
      numbers_file.write('Found!')
      break