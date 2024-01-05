# nested loop = A loop within another loop (outer, inner)
#                    outer loop:
#                        innerloop:

for x in range(3):               # 3 stands for 0,3
    for y in range(0,10):
        print(y, end="") 
    print( )


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="") 
    print( )