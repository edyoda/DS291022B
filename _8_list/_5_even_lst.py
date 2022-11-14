size=int(input("enter size:"))
lst=[]
even_lst=[]
for i in range(size):
    element=int(input("enter num:"))
    lst.append(element)
print(lst)
for i in lst:
    if i%2==0:
        even_lst.append(i)
print(even_lst)
