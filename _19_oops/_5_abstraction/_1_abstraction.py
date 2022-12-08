# Abstraction
# hiding implementation and showing functionality

# Abstract Method - method without a body and with abstractmethod decorator is known as abstract method
# Abstract Class - a class with atleast one abstract method

# we cannot create object of abstract class

from abc import ABC,abstractmethod

class Laptop(ABC):
    @abstractmethod
    def processor(self):
        pass

    @abstractmethod
    def motherboard(self):
        pass

    def keybroad(self):
        print("Helps in typing")

# laptop = Laptop()
class Programmer(Laptop):
    def processor(self):
        print("Processor")

    def motherboard(self):
        print("Motherboard")

programmer = Programmer()
programmer.keybroad()
programmer.motherboard()
programmer.processor()



