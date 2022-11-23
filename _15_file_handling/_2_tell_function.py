# Tell Function - it returns the current position of the cursor of the file

# file = open("testing.txt","w")
# position = file.tell()
# print("Before adding data : ",position)
# file.write("Good Morning!")
# position = file.tell()
# print("After adding data : ",position)


file = open("testing.txt","r")
position = file.tell()
print("Before adding data : ",position)
data = file.read()
print(data)
position = file.tell()
print("After adding data : ",position)
