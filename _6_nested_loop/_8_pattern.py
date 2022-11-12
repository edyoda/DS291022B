# for i in range(1,5):
#     for j in range(1,5):
#         mul =i*j
#         if mul<10:
#             print(mul,end='  ')
#         else:
#             print(mul,end=' ')
#     print()

row= int(input("Enter no. of row: "))
col= int(input("Enter no. of column: "))
num= 1
for i in range (1, row+1):
	for j in range (1, col+1):
		if num > 9:
			print(num, end=" ")
		else:
			print(num, end="  ")
		num += 1
	print()
