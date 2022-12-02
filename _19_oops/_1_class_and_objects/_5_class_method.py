# class method - are used to specifically deal with static/class variable

class college:

    college_name = "Edyoda"                             # class / static variable

    def __init__(self,sname,sno,saddress):              # constructor
        self.sname = sname
        self.sno = sno
        self.saddress = saddress

    def display(self):                                  # instance method
        print("Student college : ",college.college_name)
        print("Student Name : ",self.sname)
        print("Student Roll No : ",self.sno)
        print("Student Address : ",self.saddress)

    @classmethod
    def set_college_name(cls,college_name):
        cls.college_name = college_name

    @classmethod
    def get_college_name(cls):
        return cls.college_name
    


college_obj1 = college("Aryan",89,"Mumbai")
print(college_obj1.college_name)
college_obj1.display()

cname = college.get_college_name()
print("College Name : ",cname)

college.set_college_name("Coder")

cname = college.get_college_name()
print("College Name : ",cname)

