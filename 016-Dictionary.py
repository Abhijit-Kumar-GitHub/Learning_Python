# dictionary= a collection of {key:value} pairs,
#             ordered and changeable. 
#             no duplicates


capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China":"Beijing",
            "Russia": "Moscow"}

print(capitals)

# print(dir(capitals))      # to see all the different attributes and methods of dictionary
# print(help(capitals))     # to see it all in detail


# ------------------METHODS------------------

# to get one of the value from dictionary use the get funcion with key

print(capitals.get("India"))

# if python dont find the key it results in None

# to check if the key is in our dictionary
if capitals.get("Japan"):                # can replace the Japan with Russia
    print("That capital exists")
else:
    print("The capital doesnt exist")


#  to add/update the dictionary

capitals.update({"Germany":"Berlin"})

# to change the value of key

capitals.update({"USA":"New Capital"})

# to remove the key:value pair, we can use pop method

capitals.pop("China")
#------------------------>   capitals.popitem() it removes the latest/last pair in dictionary

#  to clear the dictionary
# capitals.clear()

# to get all the keys of the dictionary
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

# to get all the values of the dictionary
values=capitals.values()
print(values)

for value in capitals.values():
    print(value)

# to get all the pairs
items= capitals.items()
print(items)

for key,value in capitals.items():
    print(f"{key}:{value}")
















