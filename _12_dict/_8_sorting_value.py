num = int(input("Enter the number = "))
class_dict = dict()
for i in range(num):
  key = input("Enter keys = ")
  value = input("Enter values = ")
  class_dict[key] = value
print("OG : ",class_dict)

print("Values before sorting : ",class_dict.values())
val=class_dict.values()
val1=list(val)
for i in range(len(val1)):
    for j in range(i+1,len(val1)):
        if val1[i]>val1[j]:
            val1[i],val1[j]=val1[j],val1[i]

sorted_value = val1
print("Values after sorting : ",sorted_value)

new_dict = {}


for v in sorted_value: # ['11', '33', '55'] # v = 33
    for k in class_dict.keys(): # [5,3,1]   # k = 5
        if class_dict[k] == v:  # 33 == 33
            new_dict[k] = class_dict[k] # {3:11,5:33,1:55}

print(new_dict)



