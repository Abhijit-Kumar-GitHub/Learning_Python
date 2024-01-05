a= 89 # Python accepts the input always as string but when encountering the numerals automatically converts it into int data type

print(a,type(a))
# there are two types of type casting
# 1. Explicit Function: WE are using the {datatype_we_want}(data) or {datatype_we_want}({var_name})

c = float(a)
print(c,type(c))

# 2. Implicit Function: Python itself converts the data type
x=10.0

print(x,type(x))   # data automatically taken as float input
