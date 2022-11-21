# types of variables
# 1. local variable 
# - are defined inside the function
# - scope is within the function

# 2. global variable
# - are defined anywhere in the program
# - scope is throughout the python file

school_name = "Edyoda"

def student1():                 # local variable
    s1_name = "Bharati"                # local variable
    s1_rno = 90                        # local variable  
    global address
    address = "Mumbai"
    print("School Address for student1 function : ",address)
    print(f"Student 1 : \nName : {s1_name} \nRno : {s1_rno}")
    print(school_name)

def student2():
    s2_name = "Ram"
    s2_rno = 100
    print("School Address for student2 function : ",address)
    print(f"Student 2 : \nName : {s2_name} \nRno : {s2_rno}")
    

student1()
student2()

print(school_name)
print("School Address for outside the function : ",address)