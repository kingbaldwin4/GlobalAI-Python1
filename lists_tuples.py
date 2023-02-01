shopping_list = ["Apple", "Juice", "Ball", "Book"]

shopping_list.append("Water")
print(shopping_list)

shopping_list.insert(2,"Banana")
print(shopping_list)

shopping_list.remove("Apple")
print(shopping_list)

shopping_list[3] = "Strawberry"
print(shopping_list)


number_list = [1,2,3,4,5]

square_list = []

for num in number_list:
  square_list.append(num**2)

print(square_list)

number_list = [1,2,3,4,5]
square_list = [num ** 2 for num in number_list]

print(square_list)


shopping_list2  = ("Apple", "Juice", "Ball", "Book")
item1, item2, item3, item4 = shopping_list2
print(item1)
print(item2)
print(item3)
print(item4)

print(shopping_list2[0])

# shopping_list2[1] = "Water"  Tuples are const lists