import re 
from operations import *
import random

if __name__ == "__main__":
    while True:
        try:
            choice = int(input("Enter \n1.Register \n2.Login \n3.Exit \n"))
        except ValueError:
            print("Please enter valid choice i.e between 1-3!")
            continue

        if choice == 1:
            try:
                register_choice = int(input("Enter \n1.Register as Admin \n2.Register as Student \n3.Exit \n"))
            except ValueError:
                print("Please enter valid choice i.e between 1-3!")
                continue

            if register_choice == 1:
                name = input("Enter your name : ")
                mobile_no = input("Enter your mobile number : ")
                email_ID = input("Enter your email ID : ")
                password = input("Enter your password : ")

                name_re = re.findall(r"^[A-Za-z]+$",name)
                mobile_no_re = re.findall(r"^[1-9]{1}\d{9}$", mobile_no) 
                email_ID_re = re.findall(r"^\w+[@][a-z]+[.]com$",email_ID)
                password_re = re.findall("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%*?&!])[A-Za-z\d@#$%^&*?]{6,16}",password)

                if name_re and mobile_no_re and email_ID_re and password_re:
                    register_flag = register("admin_details.json",name,mobile_no,email_ID,password)
                    if register_flag: 
                        print("Successfully Registerd")
                    else:
                        print("Registeration Failed!")
                else:
                    if not name_re:
                        print("Entered name format is incorrect")
                        continue

                    if not mobile_no_re:
                        print("Entered mobile no format is incorrect")
                        continue

                    if not email_ID_re:
                        print("Entered email ID format is incorrect")
                        continue

                    if not password_re:
                        print("Entered password format is incorrect")
                        continue
                
            if register_choice == 2:
                name = input("Enter your name : ")
                mobile_no = input("Enter your mobile number : ")
                email_ID = input("Enter your email ID : ")
                password = input("Enter your password : ")

                name_re = re.findall(r"^[A-Za-z]+$",name)
                mobile_no_re = re.findall(r"^[1-9]{1}\d{9}$", mobile_no) 
                email_ID_re = re.findall(r"^\w+[@][a-z]+[.]com$",email_ID)
                password_re = re.findall("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%*?&!])[A-Za-z\d@#$%^&*?]{6,16}",password)

                if name_re and mobile_no_re and email_ID_re and password_re:
                    register_flag = register("student_details.json",name,mobile_no,email_ID,password)
                    if register_flag: 
                        print("Successfully Registerd")
                    else:
                        print("Registeration Failed!")
                else:
                    if not name_re:
                        print("Entered name format is incorrect")
                        continue

                    if not mobile_no_re:
                        print("Entered mobile no format is incorrect")
                        continue

                    if not email_ID_re:
                        print("Entered email ID format is incorrect")
                        continue

                    if not password_re:
                        print("Entered password format is incorrect")
                        continue

            if register_choice == 3:
                exit() 
            
        if choice == 2:
            try:
                login_choice = int(input("Enter \n1.Login as Admin \n2.Login as Student \n3.Exit \n"))
            except ValueError:
                print("Enter valid choice between 1-3!")
                continue

            if login_choice == 1:
                email_ID = input("Enter your email ID : ")
                password = input("Enter your password : ")
                login_flag = login("admin_details.json",email_ID,password)
                if login_flag:
                    print("Login Successfully!")
                    while True:
                        try:
                            module_choice = int(input("Enter \n1.Create Module \n2.View Module \n3.Update Module \n4.Delete Module \n5.Exit \n"))
                        except ValueError:
                            print("Enter valid choice between 1-5!")
                            continue

                        if module_choice == 1:
                            module_ID = random.randint(10000,20000)
                            module_name = input("Enter module name : ")
                            start_date = input("Enter start date (YYYY-MM-DD) : ")
                            end_date = input("Enter end date (YYYY-MM-DD) : ")

                            if module_ID and module_name and start_date and end_date:
                                create_module_flag = create_module("module.json",module_ID,module_name,start_date,end_date)
                                if create_module_flag:
                                    print("Module is successfully added!")
                                else:
                                    print("Module did not get added!")

                        if module_choice == 2:
                            file_data = view_module("module.json")
                            # for i in file_data:
                            #     for k,v in i.items():
                            #         print(k,"---->",v)
                            #     print()
                            for i in file_data:
                                print(i)

                        if module_choice == 3:
                            module_ID = int(input("Enter Module ID which you want to update : "))
                            module_name = input("Enter updated module name : ")
                            start_date = input("Enter updated start date (YYYY-MM-DD) : ")
                            end_date = input("Enter updated end date (YYYY-MM-DD) : ")
                            update_module_flag = update_module("module.json",module_ID,module_name,start_date,end_date)
                            if update_module_flag:
                                print("Successfully updated the module")
                            else:
                                print("Module did not get updated!")


                        if module_choice == 4:
                            module_ID = int(input("Enter Module ID which you want to delete : "))
                            delete_module_flag = delete_module("module.json",module_ID)
                            if delete_module_flag:
                                print("Successfully deleted the module!")
                            else:
                                print("Module did not get deleted!")

                else:
                    print("Login Failed!")

            if login_choice == 2:
                email_ID = input("Enter your email ID : ")
                password = input("Enter your password : ")
                login_flag = login("student_details.json",email_ID,password)
                if login_flag:
                    print("Login Successfully!")
                else:
                    print("Login Failed!")

            if login_choice == 3:
                exit()