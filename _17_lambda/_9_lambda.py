# lst=[1,2,3,4,5,6,7,8,9]
# #o/p:["odd","even",....]

# result=list(map(lambda data: "Even" if data%2==0 else "Odd",lst))
# print(result)


# lst = [12,15,18,45,90,85,45,30]

# result=list(filter(lambda data:data%3==0 and data%5==0,lst))
# print(result)


# output=list(filter(lambda data:data if data%5==0 and data%3==0 else None,lst))
# print(output)





lst = ["apple","mango","orange"]

data = list(map(lambda data : data[::-1],lst))
print(data)

result = list(map(lambda data: "".join(reversed(data)), lst))
print("\nReverse strings of fruits:",result)


