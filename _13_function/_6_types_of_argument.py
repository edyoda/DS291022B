# types of argument

# 1. required/positional argument
# 2. default argument
# 3. keyword argument
# 4. variable-length argument
    # a. Arbitrary positional argument
    # b. Arbitrary keyword argument

# 1. required / postional argument
# def add(no1,no2,no3):
#     return no1 + no2

# add(10,20,67)



# 2. default argument
# def add(no2,no1 = 10,no3=90):
#     return no1+no2

# data = add(67)
# print(data)



# 3. keyword argument
# def add(no3,no1,no2):
#     print(no1,no2)
#     return no1+no2

# data = add(no2=90,no1=10,no3=100)
# print(data)



# 4. Variable Length Argument
# a. Arbitrary Positional Argument 
# called as args
# stores the parameters in tuple

# def users(*args):
#     print(type(args))
#     print(args)
#     for i in args:
#         print(i)
#     print(args[6])

# users(1,2,3,4,5,True,"Bharati",8.9,[5,6,3,2],(7,5,3,2))


# b. Arbitrary Keyword Argument
# called as kwargs
# stores the parameters in dict

def users(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['three'])

    for k,v in kwargs.items():
        print(k,"---->",v)

users(one="Bharati",two="Ram",three="Raj")
