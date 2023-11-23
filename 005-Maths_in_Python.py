####################### ARITHEMATIC OPERATIONS

# addition
friends = 0
# friends = friends + 1
friends += 1   # using augmented assignment operator as it takes less operator and is easier to read
print(friends)

# subtraction
enemies = 30
# enemies = enemies - 2
enemies -= 2
print(enemies)

# Multiplication
candies = 5
# candies = candies * 3
candies *= 3
print(candies)

# Division
cake = 5
# cake = cake / 2
cake /= 2
print(cake)

# Exponents
toffee = 9
# toffee = toffee ** 2
toffee **= 2
print(toffee)

# Modulus operator(gives us remainder). the symbol is %
# toffee_left = toffee % 6
toffee %= 6
toffeeleft = toffee
print(toffeeleft)

#################### BUILT IN FUNCTIONS

a = 2
x = 3.149
y = -4
z = 5

# rounding off
resultround = round(x)                # rounding off to 0 decimal places or to ones place
resultround2 = round(x, 2)            # rounding off to 2 decimal places
resultround3 = round(186.564659, -1)  # rounding off to  tens places
resultround4 = round(186.564659, -2)  # rounding off to hundreds places
resultround5 = round(-186.564659, -2)

print(resultround)
print(resultround2)
print(resultround3)
print(resultround4)
print(resultround5)

# absoulute value: it gives the distance of the number away from the zero

resultabolute = abs(x)
ra2 = abs(y)
ra3 = abs(z)
ra4 = abs(a)

print(resultabolute)
print(ra2)
print(ra3)
print(ra4)

# Power function
resultpower = pow(z,a)
rp2 = pow(z,y)
rp3 = pow(-a, z)

print(resultpower)
print(rp2)
print(rp3)

# max and min function

resultmax = max(a, x, y, z)
resultmin = min(a, x, y, z)

print(resultmax)
print(resultmin)


#####################  MATH MODULE

import math

print(math.pi)
print(math.e)

resultsquareroot =  math.sqrt(x)
print(resultsquareroot)

p = 9.1
q = 9.9
resultroundup = math.ceil(p)
resultrounddown = math.floor(q)
print(resultroundup)
print(resultrounddown)









