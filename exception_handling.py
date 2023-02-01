'''
number1= 15
number2 = input('Please enter a Number: ')
print(number1 + number2)


celsius = 18
if celsius > 20:
  print('Good 🟩')
  else:
    print('Cold ❄️')'''


def divide(number1, number2):
   number1_integer = int(number1)
   number2_integer = int(number2)
   return number1_integer / number2_integer
 
number1 = input('Please provide number1: ')
number2 = input('Please provide number2: ')
 
print(divide(number1, number2))


def divide(number1, number2):
   try:
       number1_integer = int(number1)
       number2_integer = int(number2)
       return number1_integer / number2_integer
 
   except:
       return 'Only integers are allowed! Try again.'
 
number1 = input('Please provide a number1: ')
number2 = input('Please provide a number2: ')
 
print(divide(number1, number2))



def divide(number1, number2):
   try:
       number1_integer = int(number1)
       number2_integer = int(number2)
       return number1_integer / number2_integer
  
   except ValueError:
       return 'Only integers are allowed!'
 
   except ZeroDivisionError:
       return 'You cannot divide any number by zero!'



number1 = input('Please provide a number1: ')
number2 = input('Please provide a number2: ')
 
print(divide(number1, number2))