import re

def deposit(amt):
    balance = 0
    with open(r"C:\Users\vashi\OneDrive\Documents\DS291022B\DS291022B\Python\_32_atm_project\balance.txt","r") as file:
        rows = file.readlines()
        current_balance = rows[-1]
        current_balance = re.sub("\D","",current_balance)
        balance = int(current_balance)
        balance += amt
    with open(r"C:\Users\vashi\OneDrive\Documents\DS291022B\DS291022B\Python\_32_atm_project\balance.txt","a") as file:
        file.write("\nDeposited Amount : "+str(balance))
    return balance
    
def withdrawal(amt):
    balance = 0
    with open(r"C:\Users\vashi\OneDrive\Documents\DS291022B\DS291022B\Python\_32_atm_project\balance.txt","r") as file:
        rows = file.readlines()
        current_balance = rows[-1]
        current_balance = re.sub("\D","",current_balance)
        balance = int(current_balance)
        balance -= amt
    with open(r"C:\Users\vashi\OneDrive\Documents\DS291022B\DS291022B\Python\_32_atm_project\balance.txt","a") as file:
        file.write("\nWithdrawal Amount : "+str(balance))
    return balance

def mini_statement():
    with open(r"C:\Users\vashi\OneDrive\Documents\DS291022B\DS291022B\Python\_32_atm_project\balance.txt","r") as file:
        data = file.read()

    return data