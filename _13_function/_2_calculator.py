# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y

# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     choice = input("Enter choice(1/2/3/4): ")
    
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == '1':
#         print(num1, "+", num2, "=", add(num1, num2))

#     elif choice == '2':
#         print(num1, "-", num2, "=", subtract(num1, num2))

#     elif choice == '3':
#         print(num1, "*", num2, "=", multiply(num1, num2))

#     elif choice == '4':
#         print(num1, "/", num2, "=", divide(num1, num2))
#     else:
#         print("Invalid Input")

    
#     next_calculation = input("Let's do next calculation? (yes/no): ")
#     if next_calculation == "no":
#         break




def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

num1 = int(input("Enter The First Number: "))
num2 = int(input("Enter The Second Number: "))

print("Which operation would you like to perform?")
choice = input("Enter any these choice +,-,*,/ : ")

result = 0
if choice == '+':
    operation = 'Addition'
    print( add(num1, num2))
elif choice == '-':
    operation = 'Subtraction'
    print(subtract(num1, num2))
elif choice == '*':
    operation = 'Multiplication'
    print(mult(num1, num2))
elif choice == '/':
    operation = 'Division'
    print(div(num1, num2))
else:
    print("Invalid choice")
