# size=int(input('enter the size :'))
# lst=[]
# for i in range(size):
#     element=int(input('enter the element'))
#     lst.append(element)
# lst1=[]
# [lst1.append(x) for x in lst if x not in lst1]
# print(lst1)
# dict1=dict()
# for i in lst1:
#     x=[i*j for j in range(1,11)]
#     dict1[i]=x
# print(dict1)


size=int(input('enter the size :'))
lst=[]
for i in range(size):
    element=int(input('enter the element'))
    lst.append(element)
lst1=[]

for x in lst:
    if x not in lst1:
        lst1.append(x)
print(lst1) # [4,2,3]

dict1=dict()

for i in lst1: # i = 2
    x = []
    for j in range(1,11): # j = 2
        x.append(i*j)  
    dict1[i]=x
    
print(dict1)
