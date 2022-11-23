file = open("demo.txt")
file.close()

is_close = file.closed # boolean value
print("Closed : ",is_close)

file_name = file.name
print("Filename : ",file_name)

file_mode = file.mode
print("Mode : ",file_mode)