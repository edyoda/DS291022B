number = int(input("enter a number : "))

# if number % 3 == 0:
#      if number % 5 == 0:
#         print("number is divisible by 3 and 5")
#      else:
#         print("number is divisible only by 3")
# else:
#    print("not divisible by any of 3 and 5")


if number % 3 == 0 and number % 5 == 0:
    print("Number is divisible by 3 and 5")
else:
    print("It is not divisible")