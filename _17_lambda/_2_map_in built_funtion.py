lst = [67,8,1,2,4,36,5,7]

# def square(data):
#     sq_lst = []
#     for i in data:
#         sq = i**2
#         sq_lst.append(sq)
#     return sq_lst
# result = square(lst)
# print(result)


def square(data):
    return data**2

result = list(map(square,lst))
print(result)