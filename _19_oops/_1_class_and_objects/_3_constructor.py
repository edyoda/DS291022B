# Constructor
# it is a special kind of method
# it is defined using __init__()
# you need not have to call it explicitly, it gets called automatically when an object is created
# it is used to create an object
# it is use to initialize instance variable
# constructor has same name as class name
# contructor bydefault gives you an object, so it doesn't accept return statement

# NOTE : It is not recommended to write logical part in inside constructor 

# Types of constructors
# 1. Default Contructor - when you don't create a constructor of your class, then compiler provides an default contructor
# 2. Zero Contructor - contructor without parameter
# 3. Parameterized Contructor - contructor with parameter

class contructor:
    def __init__(self,name='',rno=0):
        self.name = name
        self.rno = rno

    def display(self):
        print(f'Name : {self.name} \nRoll No : {self.rno}')

obj = contructor(name="Bharati") # creating object
obj.display()

# obj1 = contructor("Maha",24) # creating object
# obj1.display()

# obj2 = contructor("Aryan",89) # creating object
# obj2.display()


