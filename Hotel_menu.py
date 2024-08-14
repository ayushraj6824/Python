menu={
    'Pizza':120,
    'Pasta':60,
    'Burger':60,
    'Salad':70,
    'Coffe':150,
}
print("Welcome to Python REstaurant")
print("Pizza: RS120\nPasta: Rs60\nBurger: Rs60\nSalad: Rs70\nCoffe: 150")
order_total=0
item_1=input("Enter the name of item you want to order :")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else :
    print(f"Ordered item {item_1} is not available yet !")

another_order=input("do you want to add another item?(Yes/No)")
if another_order=="Yes":
    order_total +=