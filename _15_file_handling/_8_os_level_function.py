import os

# deletes the file
# os.remove("demo.txt")

# checks if the given file exist or not
# is_exists = os.path.exists("edyoda.txt")
# print(is_exists)

# deletes the folder . Please note : Empty needs to be empty
# os.rmdir("C:\\Users\\vashi\\OneDrive\\Documents\\DS291022B\\DS291022B\\Python\\test")

# file = open("C:\\FileHandling\\test.txt","w")

# x mode - creates the file and if file already exist then it will throw an error
file_name = "aryan.txt"
if os.path.exists(file_name) == False:
    file = open(file_name,"x")
    print("File got created!")
else:
    print("File already exist")





