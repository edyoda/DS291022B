# Encapsulation
# it is use to bind attributes(variable) and behaviour(method) together into one single unit
# it is use to access private members through public environment

# private member - cannot be accessed outside the class

class Car:
    def __init__(self,__engine,brand,mileage):
        self.__engine = __engine                        # private member 
        self.brand = brand
        self.mileage = mileage

    def __str__(self):
        return f"Car Details : \nEngine: {self.__engine} \nBrand: {self.brand} \nMileage: {self.mileage}"

    # getter and setter

    # setter for engine
    def set_engine(self,__engine):
        self.__engine = __engine 

    # getter for engine
    def get_engine(self):
        return self.__engine

    # setter for brand
    def set_brand(self,brand):
        self.brand = brand 

    # getter for engine
    def get_brand(self):
        return self.brand

    # setter for mileage
    def set_mileage(self,mileage):
        self.mileage = mileage

    # getter for mileage
    def get_mileage(self):
        return self.mileage

car = Car("Diesel Engine","BMW","35km/l")
# data = car.get_engine()
# print(data)

# car.set_engine("Petrol Engine","Aryan")

# data = car.get_engine()
# print(data)

print("Before modification : \n",car,"\n")

car.set_mileage("45km/l")
car.set_engine("Petrol Engine")

print("After modification : \n",car,"\n")

mileage = car.get_mileage()
print("\n Mileage : ",mileage)

