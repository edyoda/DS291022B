# Set Comprehension - is use to create a new set from another set,list,tuple

nums = [1,2,3,4,5,6]
even = {i for i in nums if i%2==0}
print(even)
print(type(even))