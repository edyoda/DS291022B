file = open("edyoda.txt","w")

# data = file.read()   # read the whole data
# print(data)

# data = file.read(2)  # reads only 2 characters
# print(data)

# data = file.readline() # reads the first line
# print(data)

# data = file.readlines() # returns the list of lines
# print(data)
# del data[1]
# print(data)


# file.write("Hey")

lst = ["Hello\n","Hey\n","Bye\n","Bharati"]
file.writelines(lst)