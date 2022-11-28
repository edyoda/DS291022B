# Lambda
# it an anonymous function
# it is a function without a name
# it can have any number of arguments but can only have one expression (condition)
# it is use to create one liner function
# we don't need return statement in lambda
# can define it in another function as a argument

# Function
# needs name 
# it can have any number of expression
# return statement is required
# cannot define it in another function as a argument

# def fun(a,b):
#     return a+b

# data = fun(7,8)
# print(data)

# syntax : lambda <argument,argument1> : <expression>
data = lambda a,b : a+b
print("Data : ",data(7,8))