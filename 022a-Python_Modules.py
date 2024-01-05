# # module = a file containing code we want to include in our program.
# #          use "import" to include a module (built in or your own)
# #          it is useful to break up a large program into reusable small separate program files

# # for a list of all modules found in standard python library help("module")
# print(help("module"))
# # for all the different variables and function in a module use help("name of module")
# print(help("math"))

########_______________________________________________________________________
## First Way to import module and use it

# import math
# print(math.pi) 
######_____________________________________________________________________________

# ## Second Way to import module and use it
# import math as m
# print(m.pi)
# ## Here we are importing the function and assigning it a new name to be called as in this program
# #########__________________________________________________________________________________________

# ## Third way to import a module and use it
# ## We use this method when we are only requiring a few function or variables from a module

# from math import pi
# print(pi)        # Here we dont need to use the module prefix before the variable/function name

##  BEWARE OF CREATING A CONFLICT IN NAMESPACE WHILE ASSIGNING THE NAME OF FUNCTION OR IN THIRD WAY

import SampleModule as k
print(k.pi)

k.square(5)
k.area(10)