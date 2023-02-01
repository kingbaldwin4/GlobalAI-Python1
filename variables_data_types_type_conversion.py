name = "Michael"
age = 25

print(name)
print(age)

print(type(name))
print(type(age))

store_items = ['Apple',1.49,'Banana',1,'Milk',2.99,'Cheese',4.49]
print(store_items, type(store_items))

print(store_items[2])
print(store_items[0:4])
print(store_items[2:])
print(store_items[:2])
store_items[2] = 'Chocolate'
print(store_items)

age += 0.5
print(age, type(age))

age = int(age)
print(age, type(age))