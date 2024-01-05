# We have to make a shopping cart
# it shall ask for food and  then price of that food
#  and continue until user quits with q
# Then it shall display user's input food items and the total price for it


foods=[]
prices=[]
total=0


while True:
    food=input("Enter food you would like to buy(press q to quit): ")
    if food.lower()=="q":
        break
    else:
        price=int(input("Enter the price of it: Rs"))
        foods.append(food)
        prices.append(price)

# for food in foods:
#     print(f"The foods that I like are: {food}")

print("The foods that I like are: ")
for food in foods:
    print(food, end=" ")
print()  # to make the next print statement start at a new line

print("----- YOUR SHOPPING CART -----")

for price in prices:
    total += price

print(f"The total cost for food is: Rs {total}")









