import os       # os is a module with methods for interacting with the operating system, like creating files and directories, management of files and directories, input, output, environment variables, process management, etc.

file_path = "C:\\USED_AS_DRIVE(D)\\WORK\\PROGRAMMING\\Python(Bro_Code)\\FileHandling(BroCodePython)Directory\\test.txt"     # in path replace the backslash with double backslash as the escape sequence for \ is \\
directory_path = "C:\\USED_AS_DRIVE(D)\\WORK\\PROGRAMMING\\Python(Bro_Code)\\FileHandling(BroCodePython)Directory"

if os.path.exists(file_path):
    print("That location exists")        # This will not tell if the location is file or not
    if os.path.isfile(file_path):
        print("That is a file")
    if os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location exists")

































