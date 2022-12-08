# Dunder Method | Special Method | Magic Method

# __init__
# __str__
# __mro__ 


# print(dir(list))


# + --> __add__
# * --> __mul__

# len() --> __len__

class special:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __add__(self,self1):
        return self.salary + self1.salary 

    def __mul__(self,self1):
        return self.salary - self1.salary

    def __len__(self):
        return len(self.name)

obj = special("Ram",15000)
obj1 = special("Raj",20000)
print(obj + obj1)
print(obj * obj1)
print(len(obj))