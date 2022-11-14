# nested if - if inside if

e_name = input("Enter your name : ")
e_age = int(input("Enter your age : "))

if e_age >= 18:
    qualification = int(input("Enter your qualification : "))
    if qualification >= 15:
        experience = float(input("Enter your experience (in years) : "))
        if experience >= 1:
            print("Congrats! You are hired!")
        else:
            print("Please do an internship and re-apply in our company post that. Thank You!")
    else:
        print("Please complete your education and re-apply in our company")
else:
    print("Sorry you are still a kid!")

