# n=4;i=0
# while i<=n:
#   print(" " * (n - i) +"*" * i) # " " * 4 + * 0
#   i+=1


row= int(input("Enter no. of row: "))

for i in range (1, row+1):
	print(row*" " + i*"*", end=" ")
	row -= 1
	print()
