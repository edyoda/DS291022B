lst = []
size = int(input("Enter the number of elements ="))
for i in range(size):
  elements = int(input("Enter the elements = "))
  lst.append(elements)
print(lst)   # [3,8,1]

maximum = lst[0] # 3
for j in lst:
  if j > maximum:
    maximum = j # 8
print("Greatest number =", maximum)
