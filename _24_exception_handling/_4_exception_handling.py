# no1 = int(input("Enter no1 : "))
# no2 = int(input("Enter no2 : "))
# add = no1 + no2
# print("Addition : ",add)


try:
    no1=int(input("Enter no1: "))
    no2=int(input("Enter no2: "))
except:
    print("Enter the integer value!")
    no1=int(input("Enter no1: "))
    no2=int(input("Enter no2: "))
    
add=no1+no2
print("Added value:", add)