"""
1. Remove any '_' or ' '.
2. Add all digits in the odd places from right to left.
3. Double every second digit from right to left.
                        (If the result is a two-digit number, add the two digit number together to get a single digit.)
4. Sum the totals of steps 2 & 3.
5. If sum is divisible by 10, the credit card num is valid.
"""

sum_odd=sum_even=0
total=0

# step 1

cno=input("Enter a credit card no.: ")
cno=cno.replace("-", "")
cno=cno.replace(" ", "")

# step 2

cno=cno[::-1]
for x in cno[::2]:
    sum_odd+=int(x)
# print(sum_odd)

# step 3

for y in cno[1::2]:
    z=2*int(y)
    if z>=10:
        sum_even+= (1+(z%10))
    else:
        sum_even+=z
# print(sum_even)

# step 4

total= sum_odd + sum_even

# step 5

if total%10 == 0:
    print("Card no. is valid")
else:
    print("Card no. is invalid")










