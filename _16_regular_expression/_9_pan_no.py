import re

data = input("Enter a PAN card number: ")

result = re.findall(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$", data)
if result:
	print("The PAN card is correct")
else:
	print("Invalid PAN card number")
