class InvalidVotingError(Exception):  #(BaseException)
    # def __init__(self):
    #     print("You are still a kid! Better luck next time!")

    def __str__(self):
        return "You are still a kid! Better luck next time!"


# # Pre - inside a file store a hardcoded pin of 4 digit
# pin : 1234
# balance = 10000
# if correct 
# 1. Deposit 
#     if 1090 then raise the Exception
#     if more than 25000 than raise the Exception
# 2. Withdrawal
#     if 1090 then raise the Exception
#     if more than 25000 than raise the Exception
# 3. Mini-statement
#     show the current balance

# if not correct
# then raise the exception