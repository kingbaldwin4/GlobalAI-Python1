celsius = 25
if celsius > 20:
    print("Good 🟩")

celsius = 18
if celsius > 20:
    print('Good 🟩')

celsius = 18
if celsius > 20:
  print('Good 🟩')
else:
  print('Cold ❄️')


  celsius = 32
if celsius > 30:
  print('Hot 🔥')
elif celsius > 20:
  print('Good 🟩')
else: 
  print('Cold ❄️')


  celsius = 32
 
if celsius > 30:
  print('Hot 🔥')
elif 30 <= celsius > 20:
  print('Good 🟩')
elif -273 < celsius <= 20:
  print('Cold ❄️')
else:
  print('Something went wrong!')


drivers_licence = False
age = 18
 
if age > 17:
    if drivers_licence:
        print('You can drive car')
    else:
        print('You need to go to a drivers licence course')
else:
    print('You need to get older')