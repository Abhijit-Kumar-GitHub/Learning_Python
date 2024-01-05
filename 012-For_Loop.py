# for loops = execute a block of code a fixed nu. of times.
#             WE can iterate over a range, string, sequence, etc.

for x in range(1,11):  # here x is counter, second number is exclusive
    print(x)


for y in reversed(range(1,11)):  # here x is counter, second number is exclusive
    print(y)
print("Happy new year")

for z in range(1,11,3):
    print(z)

credit_card= "1234-5678-9012-3456"

for a in credit_card:
    print(a)

for b in range(1,21):
    if b==13:
        continue      # continue is used to skip over this iteration
    else:
        print(b)


for c in range(1,21):
    if c==13:
        continue      
    else:
        print(c)