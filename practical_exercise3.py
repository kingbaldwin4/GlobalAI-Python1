def greetings(name):
    print("Greetings ",name)

greetings("Sam")

def difference(number1, number2):
    if(number1 != number2):
        print("Chocolate prices are different from each other...")
    else:
        print("Chocolate prices are equal")

difference(14.99,12.49)


birthday = "4 September 1996"
place_of_birth = "London"
current_city = "London"

def introduction(bday,pob,cc):
    print(f'Julia birthday:{bday}, birth place:{pob} and living in:{cc}'.format(bday,pob,cc))

introduction(birthday,place_of_birth,current_city)

def change_cc(cc):
   global current_city
   current_city = "New York"

change_cc(current_city)
introduction(birthday,place_of_birth,current_city)

import seaborn as sns

day = [1,2,3,4,5,6,7]
avg_temperature = [14,9,3,11,18,27,6]
sns.barplot(x='day',y='temperature',data=day)