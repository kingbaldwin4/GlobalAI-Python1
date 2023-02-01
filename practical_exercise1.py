message = "Hello, my name is Amir! Nice to meet you. What is yours?"
print(message)
name = "Oguzhan Topal"
print("My name is ",name)
message2 = "Would you like to plan an exciting adventure with me today?"
print(message2)
answer = "Yes, Amir"
print(answer)

his_age = 20
his_height = 1.76
his_hair_color = "brunette"
his_hometown = "Iran"
where_he_lives = "Turkey"

print("I am", str(his_age),"years old,",str(his_height),"tall",his_hair_color,"guy from",his_hometown,"but I currently live in",where_he_lives)

print("What about you? Tell me about yourself.")
my_age = 24
my_height = 1.78
my_hair_color = "brown-haired"
my_hometown = "Turkey"
where_i_live = "Rize"
print("I am ", str(my_age)," years old, ",str(my_height)," tall ", my_hair_color," guy from ",my_hometown," and I currently live in ",where_i_live)
print(type(my_age),type(my_height),type(my_hair_color),type(my_hometown),type(where_i_live))


favorite_places_and_foods = ["Burger King","Whooper","McDonalds","Big Mac","Popeyes","Pop Chicken","KFC","Meal Time Menu","Pizza Hut","Jumbo Special Pizza"]
favorite_places = favorite_places_and_foods[0::2]
favorite_foods = favorite_places_and_foods[1::2]
print("Places: ",favorite_places)
print("Foods: ",favorite_foods)
print(favorite_places[:3])
print(favorite_foods[-1])

import random
import datetime
random_number = random.randint(0,2)
print("Random select: ",favorite_places_and_foods[random_number])

first_activity = "lets play chess in the park"
second_activiy = "lets play a game of tennis"
third_activity = "lets go to the museum"

first_activity_my = "play tennis"
first_activity_friend = "play chess"
print("We are going to play chess in the park! Answer: ",first_activity_my and first_activity_friend) 

second_activity_my = "go to museum"
second_activity_friend = "play tennis"

print("Let's go to the museum! Answer: ",second_activity_my or second_activity_friend) 

third_activity_my = "play chess"
third_activity_friend = "go to museum"
print("We are going to play chess in the park! Answer: ",third_activity_my and third_activity_friend) 


trip_date = input("Enter a date for travel and eating, Amir: ")
print("We are going to travel for eating on ",trip_date)
