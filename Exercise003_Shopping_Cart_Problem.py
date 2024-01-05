item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s.")
print(f"Your total is ${round(total, 2)}")  # Here, we are rounding off the decimal places to two places by system given
#  rounding tool. we take the variable in round() function then after a comma after variable in th function specify how
#  for how many decimal places we need to round off. round(variable, 5)













