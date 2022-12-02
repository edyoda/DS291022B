# Static Method - use to create utilities

sname = "Bharati"
class human:
    def __init__(self,name):
        self.name = name
    
    @staticmethod
    def utility():                          #static method
        return f"Hey {sname}"

human_obj = human("Raj")
data = human_obj.utility()
print("Name : ",data)