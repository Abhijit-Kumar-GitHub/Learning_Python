# logical operators = used on conditional statement

#           and = checks two or more conditions if True
#           or = checks if at least one condition is True
#           not = True if condition is False, and vice versa


temp = float(input("Enter the temperature in degree celsius:"))

if temp > 18 and temp < 24:   # 18 < temp < 24:
    print("The temperature is good.")
else:
    print("The temperature is bad.")

temp2 = float(input("Enter the temperature in degree celsius:"))
if temp2 <= 18 or temp2 >= 24:
    print("The temperature is bad.")
else:
    print("The temperature is good.")

sunny = True

if sunny:                   # if sunny == True
    print("It is sunny outside.")
else:
    print("It is cloudy outside.")

sunny2 = True

if not sunny2:
    print("It is cloudy outside.")
else:
    print("It is sunny outside.")















