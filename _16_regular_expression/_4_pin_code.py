import re

data = input("Enter a 6 digit Pin code: ")

result = re.findall(r"^[1-9]{1}[0-9]{5}", data)
print(result)

if result:
	print("The Pin code is correct")
else:
	print("Invalid Pin code")


