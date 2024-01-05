# #opening the file using with open will automatically close the file

# with open("C:\\USED_AS_DRIVE(D)\\WORK\\PROGRAMMING\\Python(Bro_Code)\\FileHandling(BroCodePython)Directory\\test.txt") as file:         # we can just use the file name if it is in same folder as this program
#     print(file.read()) #this will open the file and then print it line by line on terminal

# print(file.closed)     # if true that means file is closed else it is still open


#___________________________________________________________________________
# to handle exceptions as well

try:
    with open("C:\\USED_AS_DRIVE(D)\\WORK\\PROGRAMMING\\Python(Bro_Code)\\FileHandling(BroCodePython)Directory\\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found.")













