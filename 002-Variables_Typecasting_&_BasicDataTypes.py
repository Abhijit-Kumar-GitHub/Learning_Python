# Variables = a reusable container for storing a value
#             a variable behaves as if it were the value it contains

# when we create/declare a variable we give it a descriptive and unique name of what it contains
# suppose if we are working with a users age -- we can create/declare the variable "age"

# syntax for creating a variable is
# variable = value of variable

age = 21

# to print a variable-- don't include the inverted comma in the brackets as it will take that as string rather than as a
#                       variable
print(age)
print("age")    # here its taking age as the output to be printed

# to print variable with string we can do STRING CONCATENATION
# print("you are" + age + "years old") ------->>> can only concatenate str (not "int") to str{string},
# so we have to typecast[changing the variable type into another one to allow us to perform some sort of function
#      { here we are casting an int type variable character into a str type to allow us to print them together}]

# 1st method----->> pre-seeding the variable name with str and surrounding in ()
print("you are " + str(age) + " years old")   # [{<---DO KEEP SPACING IN MIND--->}]

# 2nd method----->> separating the string argument from the variable using "comma"----','
print("you are", age, "years old")

# 3rd method----->> f-string method
#                   pre-seed your quotes with f ----> then whenever we want to input variables put them in curly
#                       brackets they act as placeholder for a value or variable
print(f"you are {age} years old")

# four basic data types in python
# --INTEGER;  --FLOAT;  --STRING; --BOOLEAN;


# INTEGER-----for whole numbers

age = 21
players = 5
quantity = 9

print(f"I am {age} years old.")
print(f"There are {players} online.")
print(f"He wants to buy {quantity} pieces of chocolates.")


# FLOAT-----decimal value is accepted
#           3.0 is FLOAT whereas 3 is INTEGER

CGPA = 9.8
distance = 44.6
cost = 499.99

print(f"My grade point average is {CGPA} this year.")
print(f"Bus travelled {distance}km to reach next station.")
print(f"This jacket cost me ${cost}.")


# STRING----->> is just a series text/characters

#          ||--*** ONLY STRING VARIABLE VALUES ARE PUT IN QUOTATION MARKS AT THE TIME OF DECLARATION***
#          ||
#          ||   can contain numbers but treated as characters rather than a number on which we can perform arithmatic
#          ||   operations. For that we use INTEGER or FLOAT
#          \/
name = "Abhijit"
food = "Pizza"
email = "abhijtabhi127@gmajil.com"

print(f"My name is {name}.")
print(f"My favourite food is {food}.")
print(f"My email id is {email}.")


# BOOLEAN ---- BINARY [can only be True or False]
#              Usually used internally in programs
#           ***Case sensitive so first letter should be capital and rest running.***
#              NEVER DECLARE IT IN QUOTATION MARKS AS IT TURNS INTO STRING

online = True
forSale = False
running = True

print(f"Are you online? :{online}")
print(f"Is this item for sale? :{forSale}")
print(f"Game Running :{running}")


# Some neat tricks ---- Multiple assignment

x = 1
y = 2
z = 3

print(x)
print(y)
print(z)


a, b, c = 5, 6, 7

print(a)
print(a, b, c)
print(c)

p = q = r = 9

print(p)
print(q)
print(r)
print(p, q, r)

print("my name is " + name)
# This is possible to print without typecasting as variable "name" is already a string value
