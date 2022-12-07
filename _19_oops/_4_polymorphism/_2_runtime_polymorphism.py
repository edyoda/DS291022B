# Runtime Polymorphism - Overriding

# overriding can only be achieved in inheritance
# if your parent class method implementation is not according to what you want then 
# you can override it and write your own implementation in it

# Rules of overriding
# inheritance should be there
# child class method name should be same as parent class method
# child class should mention exact no. of parameters with same name as it is defined in parent class method

class dabba_tv(object):
    def color(self):
        print("B/W")

    def video(self):
        print("480p")

class flat_tv(dabba_tv):
    def additional_feature(self):
        print("Smart TV")

    def color(self):                 # overridden method
        print("Colored TV")

obj = flat_tv()
obj.color()


#! when a class is not inheriting any class then bydefault it inherits object class