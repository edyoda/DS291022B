# Counter

# ["a","b","a","a","c","b"]
#  a : 3 , b : 2 , c : 1

from collections import Counter

lst = ["a","b","a","a","c","b"]
counter = Counter(lst)
print(counter)

counter = Counter(a=9,c=10,b=8)
print(counter)

counter = Counter({'a': 3, 'b': 2, 'c': 1})
print(counter)