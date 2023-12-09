# indexing = accessing elements of a sequence using [] (indexing operators)
#            format is <string_name>[start:end:step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # prints the character at the first index (0=11) of the string
print(credit_number[2]) # prints the character at the third index (0,1,'2'=3) of the string
print(credit_number[4])

print(credit_number[0:4]) # prints the first 4 character, the ending index is exclusive i.e. 0,1,2,3
print(credit_number[:4]) # here python assumes that the starting index will be the begining of the string
print(credit_number[5:9])
print(credit_number[5:]) # here python assumes the ending index as the end of string

print(credit_number[-1]) # negative index starts from the right side and begins with -1,-2,-3,....
print(credit_number[-4])

print(credit_number[::2]) # print every second character of the string, starting and ending index is assumed as the start and end of the string when no value is assigned by the user
print(credit_number[::3])

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

print(credit_number[::-1]) # prints the reverse of the given string

print(credit_number.index("2")) # prints the index the first time the searched character is in the string








