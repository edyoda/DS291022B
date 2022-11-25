import re

data=input("Enter your 12 digit Aadhar number: ")
result=re.findall("^[1-9]{1}\d{3}\s[0-9]{4}\s\d{4}$",data)
if result:
    print("Valid Aadhar number")
else:
    print("Invalid")








