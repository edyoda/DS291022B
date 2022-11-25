import re
data = input("Enter a 10 digit Phone No.: ")
result = re.findall(r"^[1-9]{1}\d{9}$", data)
print(result)
if result:
	print("Entered Phone num is correct")
else:
	print("Wrong please try again")
	
	


