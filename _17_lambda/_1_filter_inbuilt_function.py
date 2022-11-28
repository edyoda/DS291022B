lst = [5,6,2,4,6,7,80,10]

# def even(data):
#     even_lst = []
#     for i in data:
#         if i%2==0:
#             even_lst.append(i)
#     return even_lst
# result = even(lst)
# print("Result : ",result)

def even(data):
    return data%2==0

result = list(filter(even,lst)) #logic,data
print(result)

for i in result:
    print(i)
