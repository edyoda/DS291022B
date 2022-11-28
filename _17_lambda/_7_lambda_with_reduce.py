from functools import reduce

lst = [5,7,3,43,54,6,76,12]

# Normal Way
# def list_sum(data):
#     sum = 0
#     for i in data:
#         sum+=i
#     return sum
# result = list_sum(lst)
# print("Result : ",result)




# Using Reduce
# def list_sum(data,data1):
#     return data + data1

# result = reduce(list_sum,lst)
# print("Result : ",result)



# Using Lambda and Reduce
result=reduce(lambda data,data1:data+data1,lst)
print("sum is:",result)
