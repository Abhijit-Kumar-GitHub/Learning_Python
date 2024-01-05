from math import sqrt, pow

h = float(input("Enter the height of the right angled triangle: "))
b = float(input("Enter the base of the right angled triangle: "))

hypotenuse = sqrt(pow(h, 2) + pow(b, 2))

print(f"The hypotenuse of the right angled triangle is: {round(hypotenuse, 2)}")
