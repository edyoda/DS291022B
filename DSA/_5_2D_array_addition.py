row = int(input("Enter no. of rows for the matrices: "))
col = int(input("Enter no. of columns for the matrices: "))

matrix1 = [] 
matrix2 = [] 
matrix = []

for i in range(row):
	rows = []
	for j in range(col):
		element = int(input("Enter element for matrix 1: "))
		rows.append(element)
	matrix1.append(rows)

for i in range(row):
	rows = []
	for j in range(col):
		element = int(input("Enter element for matrix 2: "))
		rows.append(element)
	matrix2.append(rows)

for i in range(row):
	rows = []
	for j in range(col):
		element = matrix1[i][j] + matrix2[i][j]
		rows.append(element)
	matrix.append(rows)

print("Matrix 1: \n")
for i in matrix1:
	for j in i:
		print(j, end = " ")
	print()

print("Matrix 2: \n")
for i in matrix2:
	for j in i:
		print(j, end = " ")
	print()

print("Addition of the two matrices: \n")
for i in matrix:
	for j in i:
		print(j, end = " ")
	print()

