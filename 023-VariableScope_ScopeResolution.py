# Variable Scope: where a variable is visible and accessible

# Scope Resolution: (LEGB) Local -> Enclosed -> Global -> Built-in
#                   Python first searches for the variable inn local, then enclosed(like nested function, etc), then global and finally built in


a = 5                     # this is global version of x
def func1():
    x=1                   # functions cant see in other funcitons
    y=10
    print(x)              # The variable a has a scope of local i.e. only within the function
    def func3():
        x=3
        print(x)          # Use local x, since no local y thus enclosed y is printed
        print(y)
    func3()

def func2():
    x=2
    print(x)

from math import e

print(e)                # here e is a built in variable