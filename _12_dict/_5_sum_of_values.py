# dict={'a':200,'b':800,'c':900}
# sum=0
# for key in dict:
#     sum+=dict[key]
# print(sum)


# num=int(input('enter number of items:'))
# class_list = dict() 
# total=0
# for i in range(num):
#     key = input("Enter key:")
#     value = int(input("Enter value:"))
#     total+=value
#     class_list[key] = value 

# print(class_list)
# print(total)


num=int(input("Enter number of items: "))
dct={}
for i in range(num):
    key=input("Enter key: ")
    value=int(input("Enter values: "))
    dct[key]=value
print(dct)
sum=0
val=dct.values()
for i in val:
    sum+=i
print(sum)



