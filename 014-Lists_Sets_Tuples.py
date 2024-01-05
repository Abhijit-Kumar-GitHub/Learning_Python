"""
collection=single "variable" that is used to store multiple values

    List = [] ordered and changeable. Duplicates OK
    Set = {} unordered and immutable. but add/remove OK. NO Duplicates
    Tuples () ordered and unchangeable. Duplicates OK. FASTER.

Collections can be iterated over with for loop 
"""

 
######------------------------>LISTS<----------------#######



# fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits)

# # To acces elements in list we can use index as in string

# # If index is out of range for the selected collection, it gives and IndexError
# # We can do same with index in collection that we can do in strings

# print(fruits[::2])

# for fruit in fruits:
#     print(fruit)

# # to see the different methods that are available for collection we use dir() function
# # to get description of each function use help() function
# # print(dir(fruits))
# # print(help(fruits))

# # len() returns the length of collection

# print(len(fruits))

# # to check the membership ----in and not in

# print("apple" in fruits)

# # in LIST we can change an element by assigning anothere element at the same index
# fruits[0] ="pineapple"
# print(fruit)

# # in LIST we can add an element at last with append()
# fruits.append("apple")
# print(fruits)

# # in LIST we can remove an element by remove()
# fruits.remove("orange")
# print(fruits)

# # in LIST we can insert an element at an index by insert() 
# fruits.insert(2, "grapes")
# print(fruits)

# # in LIST we can sort a list (alphabetical order) by sort()
# fruits.sort()
# print(fruits)

# # in LIST we can to find index of an element use index()
# print(fruits.index("coconut"))

# # in LIST we can to count the no. of occurences of an element in a list use count()
# print(fruits.count("banana"))

# # in LIST we can to clear a list use clear()
# fruits.clear()
# print(fruits)





######------------------------>SETS<----------------#######


# fruits = {"apple", "orange", "banana", "coconut"}

# print(fruits)

# # to see the different methods that are available for collection we use dir() function
# # to get description of each function use help() function
# # print(dir(fruits))
# # print(help(fruits))

# # len() returns the length of collection
# print(len(fruits))

# print("pineapple" in fruits)

# # IN SETS we can ADD or REMOVE elements
# fruits.add("pineapple")
# print(fruits)
# fruits.remove("apple")
# print(fruits)

# # pop() will remove whatever element is in first, and in sets that is randomised
# fruits.pop()
# print(fruits)
 
# # to clear
# fruits.clear()
# print(fruits)



######------------------------>TUPLES<----------------#######

fruits = ("apple", "orange", "banana", "coconut", "coconut")
print(fruits)

# to see the different methods that are available for collection we use dir() function
# to get description of each function use help() function
# print(dir(fruits))
# print(help(fruits))

# len() returns the length of collection
print(len(fruits))

print("pineapple" in fruits)

# in TUPLES we can to find index of an element use index()
print(fruits.index("orange"))

# in TUPLES we can to count the no. of occurences of an element in a list use count()
print(fruits.count("coconut"))


# SINCE THEY ALL ARE ITERABLE WE CAN DO THIS FOR ALL

for fruit in fruits:
    print(fruit)


