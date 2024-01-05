# Types of Arguments:
# 1. positional
# 2. DEFAULT
# 3. keyword
# 4. arbitrary


# DEFAULT ARGUMENT: a default value for certain parameters.
#                   it is used when that particular parameter is omitted, i.e. that argument is not passed
#                   makes functions more flexible and reduces the number of arguments

def net_price(list_price, discount, tax):
    return list_price * (1-discount) * (1+tax)

print(net_price(500, 0, 0.05))

# Now imagine that 90% of times there is no discount and tax is fixed at 5%.
# then instead of filling those as arguments each time the function is called we can pass them as the default values of the parameter
# then unless specified when the function is called, python will automatically assign the value of discount and tax as 0 and 0.05.

def net_price_2(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1+tax)

print(net_price_2(500))
print(net_price_2(500, 0.1))

################## ONCE A PARAMETER IS GIVEN A DEFAULT VALUE ALL THE NEXT/RIGHT PARAMETERS SHOULD ALSO HAVE A DEFAULT VALUE

import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)
count(30,15)









