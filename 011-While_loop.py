# while loop = execute some code WHILE some condition remains true
#              Always have an exit condition, AVOID INFINITY LOOP

name=input("Enter your name: ")

# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}") 

############### here we are allowing user to move onward with the program afeter not entering their name, to make this loop run infinitely until user enters the name we can use while loop

while name == "":
    print("You did not enter your name")
    name= input("Enter your name: ")

print(f"hello {name}")

age = int( input("Enter your age: "))

while age<0:
    print("Age cant be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like: ")

print("Bye")

num= input("Enter a num between 1-10: ")

while num<1 or num>10:
    print(f"{num} jis not valid")
    num= input("Enter a num between 1-10: ")

print(f"Your name is {num}")