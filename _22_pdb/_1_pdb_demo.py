import pdb

def addition(no1,no2):
    add = no1 + no2
    return add

# pdb.set_trace()               ----> which the run the file in debugger mode from the 
# line you have mention set_trace()
if __name__ == "__main__":
    no1 = input("Enter no1 : ")
    no2 = input("Enter no2 : ")
    res = addition(no1,no2)
    print("Addition : ",res)


# python -m pdb <filename> ----> this command will run the whole file in debugger mode