# function = A block of reusable code
#            place () after the functin name to invoke/call it

def happy_birthday():                               # creating a function happy_birthday
    print("Happy birthday to you!")                  # next 4 lines define waht the function will do thus indented in the function block
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_birthday()


def happy_birthday_2(name):                               # creating a function happy_birthday_2 with a parameter-> name, Parameter are basically temp variables to be used in the function block only
    print(f"Happy birthday to {name}!")                  # next 4 lines define waht the function will do thus indented in the function block
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_birthday_2("Ram")                                 # if a function has parameters then, when it is called it needs to have matching set of arguments in parenthesis
happy_birthday_2("Steve")

def happy_birthday_3(name, age):                       # here we are passing two parameters- name and age
    print(f"Happy birthday to {name}!")               
    print(f"You are {age} years old!")
    print(f"Happy birthday to you!")
    print()

happy_birthday_3("Peter", 30)                           # Thus we pass two arguments
happy_birthday_3(12, "Henry")                          # order of arguments(shortened as args) does matter as can be seen from this example. Thus it is known as positional argument.

# There are 4 types of arguments:
# 1. POSITIONAL
# 2. Default
# 3. Keyword
# 4. Arbitrary

# return - statement used to end a function and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def minus(x, y):
    z = x-y
    return z

def divide(x,y):
    z = x/y
    return z

total = add(5,3)
print(total)

print(minus(6,2))

a = int(input("Enter numerator  : "))
b = int(input("Enter Denominator: "))
print(f"result: {divide(a,b)}")

#################################

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)