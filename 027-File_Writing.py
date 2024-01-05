text = "Yoooooo\nThis is some text\nHave a good one!\n"

# with open("C:\\USED_AS_DRIVE(D)\\WORK\\PROGRAMMING\\Python(Bro_Code)\\FileHandling(BroCodePython)Directory\\test.txt", "w") as file:            # the second optional argument is the mode of opening file, by default it is "r" which is reading mode, we can change it to "w" to write in a file.
#     file.write(text)
#################### This will overwrite over anything previously present in the file.
             
###################  We can use append mode to just add some text in the pre-existing file.["a"]

with open("C:\\USED_AS_DRIVE(D)\\WORK\\PROGRAMMING\\Python(Bro_Code)\\FileHandling(BroCodePython)Directory\\test.txt", "a") as file:
    file.write(text)