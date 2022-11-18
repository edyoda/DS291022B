num = int(input("Enter the number = "))
dict1 = dict()
for i in range(num):
  key = input("Enter keys = ")
  value = input("Enter values = ")
  dict1[key] = value
print(dict1)

list1 = list(dict1.items())
print(list1)
