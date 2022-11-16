size = int(input("Enter the size of list = "))
lst = []
for i in range(size):
  element = int(input("Enter the element = "))
  lst.append(element)
print(lst)

for i in range(len(lst)):       # i =1
  for j in range(i+1,len(lst)): # j =3
    if lst[i] > lst[j]:
      lst[i],lst[j] = lst[j],lst[i]
  print(lst)
print(lst)

