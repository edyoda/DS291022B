# # class college:
# #     def __init__(self,clgname,clgaddress):
# #         self.clgname = clgname
# #         self.clgaddress = clgaddress
    
# #     def display(self):
# #         return f"The name of college : {self.clgname} \nCollege address : {self.clgaddress}"

# # class Student (college):
# #     def __init__(self, stuname , stuaddress ,clgname, clgaddress):
# #         super().__init__(clgname, clgaddress)
# #         self.stuname = stuname
# #         self.stuaddress = stuaddress

# #     def display(self):
# #         data = super().display()
# #         return f"The name of student : {self.stuname} \nStudent address : {self.stuaddress} \n{data}"


# # student = Student("Pratham", "Bhilai","Edoyoda" , "Mumbai" )
# # data= student.display()
# # print(data)







# class College:
# 	def __init__(self, college_name, college_address):
# 		self.college_name = college_name
# 		self.college_address = college_address

# 	def display(self):
# 		print(f"College Name: {self.college_name} \nCollege Address: {self.college_address}")

# class Student(College):
# 	def __init__(self, student_name, student_address, college_name, college_address):
# 		super().__init__(college_name, college_address)
# 		self.student_name = student_name
# 		self.student_address = student_address

# 	def display(self):
# 		super().display()
# 		print(f"Student Name: {self.student_name} \nStudent Address: {self.student_address}")

# student = Student("Aryan", "Delhi", "Edyoda", "Bangalore")
# student.display()






class college:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display_college(self):
        print(f"college name:{self.name} \ncollege address: {self.address}")

class student(college):
    def __init__(self,name,address,s_name,s_address):
        super().__init__(name,address)
        self.s_name=s_name
        self.s_address=s_address
    def display_student(self):
        print(f'student name: {self.s_name} \nstudent address: {self.s_address} ')
        
obj=student('RLJIT','banglore','vishnu','kurnool')
obj.display_college()
obj.display_student()
