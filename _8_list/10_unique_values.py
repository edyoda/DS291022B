size = int(input("Enter the size of list = "))
lst = []
for i in range(size):
  element = int(input("Enter the element = "))
  lst.append(element)
print(lst)

print("The original list is : ", lst)

res = []
for i in lst:
	if not(lst.count(i) > 1):
		res.append(i)
print("After removing duplictates ", res)

