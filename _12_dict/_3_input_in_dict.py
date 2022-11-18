# dit ={}
# n = int(input("enter the value :- "))
# for i in range(n):
#     key, value = input().split()
#     dit[key] = value
#     print(dit)


# num=int(input('enter number of items:'))
# class_list = dict() 
# for i in range(num):
#     key = input("Enter key")
#     value = input("Enter value")
#     class_list[key] = value 
# print(class_list)


size=int(input("Enter the number of elements need to be added in the dictionary:"))
org_dict={}
dict={}
for i in range(size):
    key, value=input("Enter the value to be added (key, value):").split()
    org_dict={key:value}
    dict.update(org_dict)
print(dict)


{'a':200,'b':800,'c':900}
1900