# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age > 100:
    print("You are too old to sign up!")    # the code after if /  else must be indented
elif age >= 18:                                 # pay attention to order of conditions for if you put >= 18 before >100
    print("You are now signed up!")             #  every no. >100 will also satisfy the >=18 thus breaking the code
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")



 


response = input("Would you like some food? (Y/N): ")

if response == "Y":                   # == is comparison operator
    print("Have some food.")
elif response == "N":
    print("No food for you.")
else:
    print("Please input valid entry!")




name = input("Please enter your name: ")

if name == "":
    print("YOU DID NOT TYPE IN YOUR NAME!")
else:
    print(f"Welcome {name}.")




# Boolean

for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is NOT for sale.")


online = False

if online:
    print("Player is online.")
else:
    print("Player is offline.")




