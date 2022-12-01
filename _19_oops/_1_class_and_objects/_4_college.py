class college:

    college_name = "Edyoda"           # class / static variable

    def __init__(self,sname,sno,saddress):
        self.sname = sname
        self.sno = sno
        self.saddress = saddress

    def display(self):
        print("Student college : ",college.college_name)
        print("Student Name : ",self.sname)
        print("Student Roll No : ",self.sno)
        print("Student Address : ",self.saddress)

# college.college_name = "Coder"

# print(college.college_name)

college_obj1 = college("Aryan",89,"Mumbai")
print(college_obj1.college_name)
college_obj1.display()

print(college.college_name)
college_obj2 = college("Laxmi",100,"Thane")
print(college_obj2.college_name)
college_obj2.display()

print(college.college_name)
college_obj3 = college("Punna",79,"Navi Mumbai")
print(college_obj3.college_name)
college_obj3.display()