### Exception
# class demo:
#     def division(self):
#         no1 = int(input("Enter no1 : "))
#         no2 = int(input("Enter no2 : "))
#         div = no1/no2
#         print("Division : ",div)
#         print("End of program")

# obj = demo()
# obj.division()



### Exception Handling
class demo:
    def division(self):
        div = 0
        no1 = int(input("Enter no1 : "))
        no2 = int(input("Enter no2 : "))
        try:
            div = no1/no2
        except ZeroDivisionError as ex: 
            print("Exception Occured : ",ex)
        print("Division : ",div)
        print("End of program")

obj = demo()
obj.division()


# try block : use to store suspicous code
# except block : use to store handling code 