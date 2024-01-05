# exception = events detected during execution that interrupt the flow of a program

# numerator = int(input("Enter numerator: "))
# denominator = int(input("Enter denominator: "))

# result = numerator / denominator
# print(result)

# here giving the denominator the value of 0 cause an error.
# Exception handling is about making sure that the error/exceptions like above example dont interuppt the normal flow of program

# a very basic form is surrounding the dangerous part of program in try block and exception block to output in case of exception
# it is much better to use multiple exception blocks first for specific exceptions then for the general exception rather than a single exception block

"""
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    print(result)
except Exception:
    print("something went wrong :( ")
"""                                            # Not good quality code
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    # print(result)                           # a good practice is to print only once there are no errors in an else block at last.
except ZeroDivisionError as e:
    print(e)                                  # A good practice to display the error as well
    print("You cant divide by zero.")
except ValueError as e:
    print(e)
    print("Enter only numbers please.")       # When we attempt to apply int() a non numeral
except Exception as e:
    print(e)
    print("Something went wrong.")
else:
    print(result)
finally:                                    # This block is always at the end. This block will always be executed. A good opportunity to close files if we have opened them.
    print("This will always be executed")



