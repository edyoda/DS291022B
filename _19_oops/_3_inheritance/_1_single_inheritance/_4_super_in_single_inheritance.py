class dad:
    def property(self):
        print("Flat and Car")

class son(dad):
    def property(self):
        super().property()
        print("Mobile and Bike")

obj = son()
obj.property()



college ---> class
create constructor and initialize college_name and college_address
create display method

student ---> class
create constructor and initialize student_name and student_address
create display method

NOTE : student should inherit college class and all calling process should be done using child class object

College Name : .....
College Address : .....
Student Name : .....
Student Address : .....
