size = int(input("Enter the number of elements you want to add in the list : "))

lst = [] # creating empty list
for i in range(size):
    element = int(input("Enter the element : "))
    lst.append(element)

print(lst)

