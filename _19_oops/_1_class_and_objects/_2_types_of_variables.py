# instance variable - variable defined inside method/constructor with self. as prefix
#                   - scope throughout the class and if you want to access it outside the class then call it via object 

college_name = "Edyoda"                # global variable
class student:
    def info(self):
        self.name = "Ram"              # instance variable
        self.rno = 78
        address = "Mumbai"             # local variable

    def display(self):
        print(f"Name : {self.name} and Rno : {self.rno} and College Name : {college_name}")

obj = student()
obj.info()
obj.display()
print("Name : ",obj.name)