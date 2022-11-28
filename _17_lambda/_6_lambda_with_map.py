lst = [67,8,1,2,4,36,5,7]



# Normal Function
# def square(data):
#     sq_lst = []
#     for i in data:
#         sq = i**2
#         sq_lst.append(sq)
#     return sq_lst
# result = square(lst)
# print(result)



# Using Map
# def square(data):
#     return data**2

# result = list(map(square,lst))
# print(result)



# Using Lambda and Map
data = list(map(lambda data:data**2,lst))
print(data)
