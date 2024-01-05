# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


n = input("Enter username: ") 

if len(n) > 12:
    print("Your username can't be more than 12 characters")

elif not n.find(" ") == -1:
    print("username can't contain spaces")

elif not n.isalpha():
    print("YOur username can't contain spaces")

else:
    print(f"welcome {n}")
























