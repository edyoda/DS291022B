# dict1 = {'a':200,'b':100,'c':600,'d':100}
# dict2 = {'a':1200,'c':200,'b':300}
# for k in dict1:
#      if k in dict2:
#           dict2[k]=dict1[k]+dict2[k]
#      else:
#           dict2[k]=dict1[k]
# print(dict2)

dict1={'a':200,'b':100,'c':200,'d':400}
dict2={'a':1000,'b':200,'c':100}
dict3={}
for i in dict1.keys():
    for j in dict2.keys():
        if i==j:
            value=dict1[i]+dict2[j]
        elif i!=j:
            value=dict1[i]
    dict3[i]=value
print(dict3)




