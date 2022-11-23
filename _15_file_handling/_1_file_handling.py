# File Handling
# interacting with files using python is file handling

# Types of files
# text file
# binary file

# Modes for text files
# r - read (bydefault) - It will raise error if file doesn't exist. 
#                        It allows us to read the data from file                 
# w - write - It checks if file exist. 
#             If it exist, it will override that file else it will create that file
#             It allows to write the data in the file
# a - append - It creates the file if not exist.
#              If exist, it doesn't override it, instead it appends the data to the existing data
#              It allows to write the data in the file   
# r+  -        Same like read mode but it also allows to write the data
# w+  -        Same like write mode but it also allows to read the data
# a+  -        Same like append mode but it also allows to read the data

# Modes for binary files 
# rb
# wb
# ab
# rb+
# wb+
# ab+

# write mode
# open(filename,<mode>)
# file = open("demo.txt","w")
# file.write("Good Night")
# file.close()


# read mode
# file = open("demo.txt")
# data = file.read()
# print(data)


# append mode
# file = open("test.txt","a")
# file.write("All")
# file.close()


# r+ mode
file = open("test.txt","r+")
file.write("Edyoda")
file.seek(0,0)
data = file.read()
print(data)


# w+ mode
file = open("testing.txt","w+")
file.write("Testing w+ mode")
file.seek(0,0)
data = file.read()
print(data)


# a+ mode
file = open("new.txt","a+") # 0
file.write("Hey") # 012
file.seek(0,0)
data = file.read()
print(data)
