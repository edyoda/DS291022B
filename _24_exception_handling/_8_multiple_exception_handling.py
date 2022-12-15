try:
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    div = no1/no2
    print("Division : ",div)
except (ZeroDivisionError,ValueError) as ex:
    print("Error : ",ex)

print("Ends here")