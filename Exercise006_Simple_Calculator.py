num1 = float(input("Enter 1st number: "))
operator = input("Enter an operator from (+ - * /): " )
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 4))
elif operator == "-":
    result = num1 - num2
    print(round(result, 4))
elif operator == "*":
    result = num1 * num2
    print(round(result, 4))
elif operator == "/":
    result = num1 / num2
    print(round(result, 4))
else:
    print(f"{operator} is not a valid operator.")
