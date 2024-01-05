# Types of Arguments:
# 1. positional
# 2. default
# 3. KEYWORD
# 4. arbitrary

# Keyword argument : an argument preceded by an identifier.
#                    helps with the readability
#                    order of arguments dont matter

#########  NO POSITIONAL ARGUMENT MAY FOLLOW KEYWORD ARGUMENT

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr.", "Spongebob", "Squarepants")
hello("Hello", "Squarepants", "Mr.", "Spongebob")

# Kwarg
hello("hello", title="Mr.", first="Spongebob", last="Squarepants")
hello("hello", last="Squarepants", title="Mr.", first="Spongebob" )

#----------------------------------------------------------------------------------

for x in range(1,11):
    print(x,end=" ")         # here this end is also a kwarg of print function
print()

print("1", "2", "3", "4", "5", sep="-")     # sep as well is a kwarg of print function

#############3

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area= 123, first=456, last=7890)

print(phone_num)







































