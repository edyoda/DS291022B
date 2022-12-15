# finally block - the code inside finally block will execute regardless of whether exception has
# occured or not

# closing a file
# closing database

try:
    print(10/5)
except Exception as ex:
    print(ex)
finally:
    print("File closing...")

print("End of program")