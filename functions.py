number = '15'
print('Type of number before int() function: ', type(number))
 
number = int(number)
 
print('Type of number after int() function: ', type(number))

def hello(name):
  print('Hello ', name)

hello("Oguzhan")

def sum(number1, number2):
  print("Sum: ",number1 + number2)

result = sum(6,8)
print("Result: ",result)


def sum(number1, number2):
  answer = number1 + number2
  return answer
 
result = sum(6, 8)
print("Result: ",result)