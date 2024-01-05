# """ Create and print menu
#     let user choose his food in a cart
#     show food in cart
#     show total for the food"""



menu = {"pizza": 300,
        "nachos": 150,
        "popcorn": 200,
        "fries": 250,
        "chips": 100,
        "pretzel": 180,
        "soda": 120,
        "lemonade": 100}

cart = []
total = 0

print("----------------MENU---------------")
for key, value in menu.items():
    print(f"{key:10}: Rs{value}")
print("-----------------------------------")

while True:
    food= input("Select an Item (press q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print()
print("------------Your Selection------------")
for food in cart:
    total= total+menu.get(food)
    print(food, end=" ")
print()

print(f"Total is: Rs{total}")