phone_book = {'Deniz Kaya':'+90 505 123 45 67', 'Selin Demir': '+49 157 12345678', 'Ali Can':'+1 234 235 5678'}
print(phone_book)

print(phone_book['Deniz Kaya'])


inventory = dict()
inventory['bananas'] = 25
inventory['apples'] = 102
inventory['oranges'] = 54
inventory['watermelons'] = 4

print(inventory)

print(inventory['apples'])

print(inventory.keys())

print(inventory.values())

print(inventory.items())

for element in inventory:
    print(element)

for key in inventory:
    inventory[key] += 100
    print(inventory)

for key, value in inventory.items():
    if value > 200:
        print('Too many', key)
    else:
        print('Enough', key)