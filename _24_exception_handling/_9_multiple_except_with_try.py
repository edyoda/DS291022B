try:
    str1 = None
    print(len(str1))
    print(10/0)
except ZeroDivisionError as ex:
    print("You are trying to divide value by zero, which is not possible logically")
except ValueError as ex:
    print("Expected I/P doesn't match with given I/P")
except TypeError as ex:
    print("len() is not available for NoneType data")
except Exception as ex:
    print("Exception")