shopping_list = ["Milk","Apples","Orange","Potatoes"]
shopping_list.append("Bananas")
shopping_list.insert(3,"Onions")

print(shopping_list)

shopping_list.remove("Potatoes")

print(shopping_list)

shopping_list2 = [("Grapes","Fruits"),("Apples","Fruits"),("Onions","Vegetables"),("Cucumber","Vegetables")]

for x in shopping_list2:
    item1,item2 = x

    print("You can find the {0} in the {1} section".format(item1,item2))


shopping_list3 = dict()
shopping_list3["Apricot"] = "Fruits"
shopping_list3["Garlic"] = "Vegetables"
shopping_list3["Peach"] = "Fruits"
shopping_list3["Corn"] = "Vegetables"

print(shopping_list3.keys)
print(shopping_list3.values)
print(shopping_list3.items)


inventory = {'Laptop':[15000,0,'Computers'],
             'IPhone':[10000,20,'Phones'],
             'Scopy':[800,30,'Headphones']}

shopping_list4 = [('Laptop',2),('IPhone',6),('Scopy',15)]

def check_stock():
   shopping_list_update = []
   for item in shopping_list4:
    item1 = item
    if inventory[item1][1] != 0:
        if inventory[item1][1] >= item1[1]:
            print("Stock amount is enough for {0}".format(inventory[item1][1]))
        else:
            print("Stock amount is not enough for {0}".format(inventory[item1][1]))
            shopping_list4.remove(item1)


def compute_bill():
    bill = 0
    for item in shopping_list4:
        item1 = item
        bill += inventory[item1][0]*item1[1]
    
    print("Total bill is {0}".format(str(bill)))



def update_stock():
    for item in shopping_list4:
     item1 = item
     inventory[item1][1] -= item1[1]
     print("The remaining stock amount for {0} is: ".format(inventory[item1][1]))


check_stock()
compute_bill()
update_stock()

     
    