PIN = 1234
BALANCE = 10000


class DepositError(Exception):
  pass

class WithdrawalError(Exception):
  pass


def deposit(amount):
  if amount < 1090:
    raise DepositError("Deposit amount must be at least 1090.")
  if amount > 25000:
    raise DepositError("Deposit amount cannot be more than 25000.")
  
  
  BALANCE += amount


def withdrawal(amount):
  if amount < 1090:
    raise WithdrawalError("Withdrawal amount must be at least 1090.")
  if amount > 25000:
    raise WithdrawalError("Withdrawal amount cannot be more than 25000.")
  
 
  BALANCE -= amount


def mini_statement():
  print(f"Your current balance is: {BALANCE}")


try:
  deposit(1000)
except DepositError as e:
  print(e)

try:
  withdrawal(1000)
except WithdrawalError as e:
  print(e)


mini_statement()
