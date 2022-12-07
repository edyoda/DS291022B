# if there is some data in parent class which you don't want your child class to have access to
# then we you can make it private and restrict it's access.


class dad:
    def __init__(self,flat,car,FD):
        self.flat = flat
        self.car = car
        self.__FD = FD

    def __shares(self):
        print("Shares")

class son(dad):
    pass

obj = son("3BHK","BMW",1000000)
print(obj.flat)
print(obj.car)
# print(obj.__FD)

# obj.__shares()