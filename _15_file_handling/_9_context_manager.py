# Context Manager

# file = open("file_name","mode")
with open("punna.txt","w") as file: 
    file.write("Hello")
    
print(file.closed)
