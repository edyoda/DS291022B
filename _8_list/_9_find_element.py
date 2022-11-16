size=int(input("Enter the number of elements need to be added in the list:"))
org_lst=[]
new_lst=[]
for i in range(size):
    value=int(input("Enter the value to be added:"))
    org_lst.append(value)
print(org_lst)

flag = False
value1=int(input("Enter the value to be checked:"))
for i in range(size):
    if org_lst[i]==value1:
        # print("Yes, entered value is present in the list")
        flag = True
        break
    else:
        # print("No, entered value is not present in the list")
        flag = False

if flag:
    print("Yes, entered value is present in the list")
else:
    print("No, entered value is not present in the list")