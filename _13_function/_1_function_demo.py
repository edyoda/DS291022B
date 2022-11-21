# print()
# len()
# input()
# int()
# float()

# Function
# it is use to store a set of code which can be reused. 
# you can sue the same set of code with little modification if needed (parameters/argument)

# Syntax 
# def <function_name>():
#    <logic,code>

# def add():
#     no1 = int(input("Enter no1 : "))
#     no2 = int(input("Enter no2 : "))
#     addition = no1 + no2
#     print("Addition : ",addition)

# add()


def square_of_keys():
    dic1={}
    for i in range(1,16):
        value=i*i
        dic1[i]=value # i**2
    print(dic1)

# square_of_keys()
# square_of_keys()
# square_of_keys()
# square_of_keys()
# square_of_keys()

for i in range(5):
    square_of_keys()



