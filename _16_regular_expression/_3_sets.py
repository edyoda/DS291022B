import re

# data = "Python is a high level programming language! 123 _"
# result = re.findall('[isalrz]',data) # checks if the data contains i,s,a,l,r,z characters
# print(result)

# data = "Python is a high level programming language! 123 _"
# result = re.findall('[^PBN]',data) # returns characters which are not P,B,N
# print(result)

# data = "Python is a high level programming language! 123 _"
# result = re.findall('[c-m]',data) # returns characters which between c and m
# print(result)

# data = "Python is a high level programming language! 123 _"
# result = re.findall('[51290]',data) # returns digits which are either 5/1/2/9/0
# print(result)

# data = "78 56"
# result = re.findall('[0-9][8-9]',data) # returns 2 digit values if it satisfy the conditions
# print(result)

# data = "Python is a high level programming language! 123 _ @"
# result = re.findall('[@]',data) # returns if data contains '@'
# print(result)

data = "Python is a high level programming language! 123 _ @"
result = re.findall('[a-z]{5}',data) # returns if data contains '@'
print(result)