import math

radius = float(input("Enter the radius of circle in cm: "))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius,2)

print(f"The circumference of the circle is: {round(circumference, 2)} cm")
print(f"The area of the circle is: {round(area, 2)} cm^2")



