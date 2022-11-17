string= input("input string: ")
dic=dict()
for i in string.lower():
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)




