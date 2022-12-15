# Generator

# generators are function
# it is memory efficient
# it doesnot allocate memory to all the objects at the same time
# it yeilds the data and returns the element of the data when it is demanded

def fun(n):
    yield n*2

result = fun(10)
print(next(result))

# when you call next method
# 1. it is returning object to you
# 2. it is allocating memory to the object
# 3. it is deleted the object as well

gen = (2*i for i in range(1,11)) # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
print(gen)

print(next(gen))
print(next(gen))
