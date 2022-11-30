# syntax :
# class <class_name>:
#     body

# Class - It is the blueprint(planning)
# Object - It is the instance of the class
# Methods - functions which are created inside the class are known as methods!
#         - every function defined inside the class must have 'self' keyword as first parameter        
# self    - it's a keyword
#         - it represents current class object

class Building:                                                    # class
    def doors(self,no_of_doors):                                   # method
        print(f"Building has total {no_of_doors} Doors!")

    def windows(self):
        self.doors(78)
        print("Building has 80 Windows!")

building_obj = Building()                                    # object creation
building_obj.doors(50)                                       # calling method via object
building_obj.windows()

building_obj1 = Building()




