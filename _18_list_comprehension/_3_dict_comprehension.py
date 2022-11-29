# Dict Comprehension - it is use to create new dict from another type of data

# str1 = "Python"
# dict_comp = {i.upper():i.lower() for i in str1}
# print(dict_comp)




# key = [1,2,3,4,5]
# values = ["ram","raj","sunny","laxman","sita"]

# dic = {key[i] : values[i] for i in range(len(key))}
# print(dic)

# data = {i:j for (i,j) in zip(key,values)}
# print(data)


lst = [6,1,4,5,67]

dic = {k : [k*j for j in range(1,11)] for k in lst}

print(dic)


