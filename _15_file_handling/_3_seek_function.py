# seek() - it allows you to modify the position of cursor
# seek(offset,from_what)
# offset - no. of position to shift
# from_what - point of reference

# from_what only accepts 3 values
# 0 - beginning of the value  (bydefault)           
# 1 - current position of the file
# 2 - end of the file


file = open("demo.txt","w")
cur_pos = file.tell()
print("Current Position before : ",cur_pos)
file.seek(4,0)
cur_pos = file.tell()
print("Current Position after : ",cur_pos)
file.write("Hey")
cur_pos = file.tell()
print("Current Position after adding data : ",cur_pos)
