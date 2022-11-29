# List Comprehension - it is use for creating a new list from another list,set,tuple

# for i in lst:
#     if condition:
#         body

# syntax
# [body for i in lst if condition]

# nums = [1,2,3,4,5,6,7]

# Using Normal Way
# new_lst = []
# for i in nums:
#     new_lst.append(i)

# print(new_lst)


# Using List Comprehension
# data = [i for i in nums]
# print(data)






nums = [1,2,3,4,5,6,7]

# new_lst = []
# for i in nums:
#     if i%2==0:
#         new_lst.append(i)
# print(new_lst)

# data = [i for i in nums if i%2==0]
# print(data)



# string = 'Python'
# data = [i for i in string]
# print(data)



# lst=["apple","mango","ac","laptop","aeroplane","mobile","diary"]
# result=[str1 for str1 in lst if str1.startswith('a') and len(str1)>4]
# print("new list:",result)


# lst = ["apple","mango","ac","laptop","aeroplane","mobile","diary"]
# data = [i for i in lst if i[0]=='a' and len(i)>4]
# print(data)




lst = [16,78,4,5,62,12,34]
data = [lst[i] for i in range(len(lst)) if i%2 != 0]
print(data)


data = lst[1::2]
print(data)


result=[i for i in lst if lst.index(i)%2!=0 ]
print(result)


data = [i for i in lst[1:len(lst):2]]
print(data)

