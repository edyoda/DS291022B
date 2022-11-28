from functools import reduce

lst = [5,7,3,43,54,6,76,12]

# def list_sum(data):
#     sum = 0
#     for i in data:
#         sum+=i
#     return sum
# result = list_sum(lst)
# print("Result : ",result)

def list_sum(data,data1):
    return data + data1

result = reduce(list_sum,lst)
print("Result : ",result)