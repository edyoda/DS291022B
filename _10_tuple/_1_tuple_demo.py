# tuple
# [] / tuple()
# allows duplicates
# immutable
# heterogenous
# ordered
# indexed
# iterable

tup1 = (5,6,2,6,8,9,1,10)
tup2 = (15,16,12,16,18)
# print(tup)

# for i in tup:
#     print(i)

methods = dir(tuple) 
print(methods) # ['count', 'index']

indexed = tup1.index(10)
print(indexed)

counter = tup1.count(6)
print(counter)

data = tup1 + tup2
print(data)
