import re

data = input("Enter the password: ")

# result = re.findall(r"(^.*[A-Z].*[a-z].*\d.*[!@#$%^&*()]){8}$", data)
result = re.findall("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%*?&!])[A-Za-z\d@#$%^&*?]{6,16}",data)
print(result)

if result:
    print("The password is valid")
else:
    print("Invalid password")


