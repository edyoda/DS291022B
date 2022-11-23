file = open("edyoda.txt", "r")

count = 0
data =  file.readlines()

for i in data:
	count += 1

print("Number of lines: ", count)

for i in file:
	count += 1

print("Number of lines: ", count)
