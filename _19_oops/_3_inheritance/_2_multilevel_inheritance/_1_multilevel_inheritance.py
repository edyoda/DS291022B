class grandpa:
    def field(self):
        print("Field")

class dad(grandpa):
    def flat(self):
        print("Flat")
    def car(self):
        print("Car")

class son(dad):
    def bike(self):
        print("Bike")
    def mobile(self):
        print("Mobile")

obj = son()
obj.bike()
obj.mobile()
obj.flat()
obj.car()
obj.field()