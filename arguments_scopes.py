def argument_printer(arg_position1, arg_position2):
   print('Argument at position 1:', arg_position1)
   print('Argument at position 2:', arg_position2)

argument_printer('value 1', 'value 2')

def greetings(first_name, last_name, auto_correction):
  if auto_correction == True:
    capitalized_first_name = first_name.capitalize()
    capitalized_last_name = last_name.capitalize() 
    print("Hello,", capitalized_first_name, capitalized_last_name) 
  else: 
    print("Hello,", first_name, last_name)

greetings('deNiZ', 'kaYa', True)
greetings('deNiZ', 'kaYa', False)


def greetings(first_name, last_name, auto_correction = True):
  if auto_correction == True: 
    capitalized_first_name = first_name.capitalize()
    capitalized_last_name = last_name.capitalize() 
    print("Hello,", capitalized_first_name, capitalized_last_name) 
  else: 
    print("Hello,", first_name, last_name)

greetings('deNiz', 'kAYa')


def car(brand, model, colour):
    print('My favourite car is the', brand, model, 'in the colour', colour)

car('Audi', 'R8', 'black')
car(colour = 'black', model = 'R8', brand = 'Audi')
#car(colour = 'Audi', model = 'R8', 'black') error


number = 13 #Global Variable
 
def change_number():
    number = 4 #Local Variable
 
change_number()
print(number)

'''
error code for learning
#number = 13
 

 
def change_number():
 num = 4
 
change_number()
print(num)
'''

number = 13
 
def change_number():
 global number 
 number = 4
 
change_number()
print(number)


number = 13
 
def change_number(num): 
 num = 4
 return num
 
number = change_number(number)
print(number)

