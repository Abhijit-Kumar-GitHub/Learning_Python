weight = float(input("Enter the weight here: "))
unit = input("Enter K for Kilograms and L for pounds: ")

if unit == "K":
    weight *= 2.205
    unit = "Pounds"
    print(f"The weight is {round(weight, 4)} {unit}.")

elif unit == "L":
    weight /= 2.205
    unit = "Kilograms"
    print(f"The weight is {round(weight, 4)} {unit}.")

else:
    print("You have entered wrong unit!")










