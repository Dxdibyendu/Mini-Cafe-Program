#Menu of restaurant
menu = {
    'Coffe':40,
    'Pizza':60,
    'Pasts':40,
    'Burger':50,
    'Cold Coffe':60,
}

#Greet the coustomer
print("Welcome to PY-Cafe\nAvailabel item are")
print("Coffe: Rs40\nPizza: Rs60\nPasta: Rs40\nBurger: Rs50\nCold Coffe: Rs60")
order_total=0
item1=input("Enter the name of item you want to order :")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been added to your order")
else:
    print(f"Ordered item {item1} is not availabel yet!")

another_order = input("Do you want to add another item?(Yes/No)")
if another_order == "Yes" :
    item2 = input("Enter the name of the second item:")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Item {item2} has been added to order")
    else:
        print(f"Order {item2} item is not available!")
    
print(f"The total amount of items is {order_total}")
