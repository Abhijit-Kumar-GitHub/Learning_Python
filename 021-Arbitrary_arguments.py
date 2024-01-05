# Types of Arguments:
# 1. positional
# 2. default
# 3. keyword
# 4. ARBITRARY-  meaning a varying amount of arguments
#                prefix the args/kwargs with */**
#                * : unpacking operator


#                there are two types of arbitrary arguments
#                1) arbitrary (positional/default) arguments [*args] : allows to pass multiple non-key arguments
#                when we invoke a function which has *args as parameters, we pack all those arguments in TUPLES

#                2) arbitrary keyword arguments  [**kwargs] :  allows to pass multiple keyword arguments
#                when we invoke a function which has **kwargs as parameters, we pack all those arguments in DICTIONARY


def add(a, b):
    return a+b

print(add(1,2))
#print(add(1,2,4))             #this will not work as there are three arguments passed for 2 parameters, we can again define a new function to add 3 variables,
                            #    but how many custom functions need to be defined to add varying # variables. 
                            #   Thus we create a general function which can accept any amount of arguments using arbitrary arguments

def add_2(*args):                                 # we can use the name as *nums, then for num in nums: but by naming convention we generally stick to *args
    #print(type(args))                            # to check the type of *args is tuple or not
    total = 0
    for arg in args:
        total += arg
    return total

print(add_2(9))
print(add_2(8,6,8,9,6,5))

############################################################################################################################################################################

def dispaly_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()    

dispaly_name("Ram")
dispaly_name("Sunkara", "Sanmukha", "Sai", "Krishna")

################################################################################################################################################################################

###############################################################################################################################################################################

def print_address(**kwargs):
    #print(type(kwargs))
    for value in kwargs.values():
        print(f"value: {value}")

    for key in kwargs.keys():
        print(f"keys: {key}")

    for key, value in kwargs.items():
        print(f"{key}:{value}")

# if we have an incomplete function that we intend to complete later, we can write <pass> in it's block and the interpreter will ignore that function and allow the program to run

print_address(street="213 Fake Street",
              apt="100",
              city="Imaginary City",
              state="False State",
              zip="123456")

###################################################################################################################################################################################

def shipping_label(*args, **kwargs):                     # **kwargs gotta follow the *args as positional arguments cant follow keyword arguments
    for arg in args:
        print(arg, end=" ")
    print()
    
    print(f"{kwargs.get('apt')} {kwargs.get('street')}")                        # using '' single quotes as two layers of "" double quote will confuse the python interpretor
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')} {kwargs.get('country')}")


shipping_label("Patrick",
               apt="what",
               city="No",
               country="way")

shipping_label("Dr.", "Spongebob", "Harold", "Sqaurepants", "III",
              street="213 Fake Street",
              apt="100",
              city="Imaginary City",
              state="False State",
              zip="123456")

################################################################
##### here those parameters which are not passed as an arg/kwarg will return as None by default to avoid that in output , we can define functiona as:

def shipping_label(*args, **kwargs):                    
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('apt')} {kwargs.get('street')}")                       
    else:
        print(f"{kwargs.get('street')}")
    # similary a loop can be created to just print whatever is present as argument only
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')} {kwargs.get('country')}")


shipping_label("Patrick",
               apt="what",
               city="No",
               country="way")

shipping_label("Dr.", "Spongebob", "Harold", "Sqaurepants", "III",
              street="213 Fake Street",
              apt="100",
              city="Imaginary City",
              state="False State",
              zip="123456")

