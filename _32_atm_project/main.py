from exceptions import InvalidPinError,InvalidRangeError,InvalidAmountError
from operations import deposit,withdrawal,mini_statement

if __name__ == "__main__":
    pin = int(input("Enter your pin : "))
    with open(r"C:\Users\vashi\OneDrive\Documents\DS291022B\DS291022B\Python\_32_atm_project\pin.txt","r") as file:
        text_pin = file.read()

    if pin == int(text_pin):
        balance = 5000
        print("Successfully Logged In!")
        choice = int(input("Enter \n1.Deposit \n2.Withdrawal \n3.Mini-statement : \n"))

        if choice == 1:
            deposit_amt = int(input("Enter amount which you want to deposit : "))
            if deposit_amt > 25000:
                try:
                    raise InvalidRangeError()
                except Exception as ex:
                    print(ex)
            elif deposit_amt % 100 != 0:
                try:
                    raise InvalidAmountError()
                except Exception as ex:
                    print(ex)
            else:
                bal = deposit(deposit_amt)
                print("Successfully Deposited")

        elif choice == 2:
            withdrawal_amt = int(input("Enter amount which you want to withdraw : "))
            if withdrawal_amt > 25000:
                try:
                    raise InvalidRangeError()
                except Exception as ex:
                    print(ex)
            elif withdrawal_amt % 100 != 0:
                try:
                    raise InvalidAmountError()
                except Exception as ex:
                    print(ex)
            else:
                bal = withdrawal(withdrawal_amt)
                print("Successfully Withdrawal")
        
        elif choice == 3:
            data = mini_statement()
            print(data)
    else:
        try:
            raise InvalidPinError()
        except Exception as ex:
            print(ex)



