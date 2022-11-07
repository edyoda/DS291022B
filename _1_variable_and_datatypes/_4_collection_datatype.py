# list
# it is use to store more then one element in a variable
# it is represented by [] and list()
# it accepts duplicate values
# indexed-based (indexing starts with 0)
# it accepts heterogenous data (values of different datatypes)
# mutable (changeable)
# ordered
# iterable

# lst = [4,1,6,7,10,6,6,7.8,"Bharati",True]

# print(lst)
# print(type(lst))

# to retrieve specify value i.e 10
# print(lst[4])

# to modify the value which is on 4th position
# lst[4] = 100
# print(lst)

# lst1 = list([1,7,81,2,9])
# print(lst1)
# print(type(lst1))




# tuple
# () and tuple()
# duplicates are accepted
# ordered
# heterogenous data accepted
# indexed-based
# iterable
# immutable (unchangable)

# tup = (4,5,6,1,6,8,9,7.8)
# print(tup)
# print(type(tup))

# to retrieve specify value i.e 7.8
# print(tup[7])

# as tuple is immutable, we cannot modify tuple, it throws an error
# tup[7] = 900
# print(tup)



# set 
# {} and set()
# unordered
# duplicates are not allowed
# iterable
# non-indexed
# heterogenous data accepted
# mutable

set_demo = set({1,2,3,4,5})
print(set_demo)

# set_demo = {4,5,6,1,900,3,6,7,4.5,"Bharati"}
# print(set_demo)
# print(type(set_demo))

# # set is non-indexed based, so below line of code throws an error
# # print(set_demo[4])

# set_demo.add(100)
# print(set_demo)



# dict - dictionary
# key - value  ---> item
# {} and dict()
# non-indexed
# key should be unique
# value can be duplicate
# unordered
# heterogenous accepted
# mutable

# students = {'a':"Mahesh",'b':"Shailesh",'c':"Mahesh"}
# print(students)
# print(type(students))

# print(students['b'])

# students["c"] = "Bharati"
# print(students)
