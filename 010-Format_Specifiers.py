# format specifiers = {value:flags} format a value based on what flags are inserted

# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate the positive value
# := = place sign to the leftmost position
# :  = insert a space before positive numbers
# :, = comma separator for every 1000
# :0

price1= 36857464.564321
price2= -45653.633343163574
price3= 89463414631.36854568441

print(f"Price 1 is {price1}")
print(f"Price 2 is {price2}")
print(f"Price 3 is {price3}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print(f"Price 1 is {price1:.3f}")
print(f"Price 2 is {price2:.3f}")
print(f"Price 3 is {price3:.3f}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print(f"Price 1 is {price1:30}")
print(f"Price 2 is {price2:30}")
print(f"Price 3 is {price3:30}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print(f"Price 1 is {price1:030}")
print(f"Price 2 is {price2:030}")
print(f"Price 3 is {price3:030}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print(f"Price 1 is {price1:<30}")
print(f"Price 2 is {price2:<30}")
print(f"Price 3 is {price3:<30}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print(f"Price 1 is {price1:>30}")
print(f"Price 2 is {price2:>30}")
print(f"Price 3 is {price3:>30}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print(f"Price 1 is {price1:^100}")
print(f"Price 2 is {price2:^100}")
print(f"Price 3 is {price3:^100}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3:+}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print(f"Price 1 is {price1: }")
print(f"Price 2 is {price2: }")
print(f"Price 3 is {price3: }")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print(f"Price 1 is {price1:,}")
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3:,}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

print(f"Price 1 is {price1:+20,.2f}")
print(f"Price 2 is {price2:+22,.4f}")
print(f"Price 3 is {price3:+20,.2f}")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")



 