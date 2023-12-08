name=input("Enter your name: ")

result1 = len(name) #includes the spaces in the string
print(result1)

result2 = name.find("i")  # finds the first occurence of the searched character from left
print(result2)

result3 = name.rfind("i")  # finds the first occurence of the searched character from right i.e. last
print(result3)

result4 = name.find("n") # if the python is unable to find the given character then it gives the value.
print(result4)

name1 = name.capitalize() # capitalizes the first character of the string
print(name1)

name2 = name.upper() # makes all the characters uppercase
print(name2)

name3 = name.lower() # makes all the characters lowercase
print(name3)

result5 = name.isdigit()   # returns True only if the string only contains digits
print(result5)  

result6 = name.isalpha()  # returns True only if the string only contains alphabets. Space is not an alphabet 
print(result6)

tn = input("Enter your telephone no. ")

tn1 = tn.count("-")  # counts the no the specified character in the string
print()

tn2 = tn.replace("-", " ") # replaces the first charcter in the tuple with the second one. if second character is "" i.e. deletes the first character.
print(tn2)

# for the comprehensive list use    #####         print(help(str))            ###########





