def bodmas():
    equation = ""
    num_size = int(input("Enter the size of numbers you want : "))
    sym_size = int(input("Enter the size of symbols you want : "))
    num_lst = []
    sym_lst = []
    for i in range (num_size):
        number = int(input("Enter the number : "))
        num_lst.append(number)
    for i in range (sym_size):
        symbol = input("Enter the symbol : ")
        sym_lst.append(symbol)

    print(num_lst)
    final = 1
    for i in range(len(num_lst)):
        if '/' in sym_lst:
            eq = num_lst[i] / num_lst[i+1]
            print(num_lst[i] , num_lst[i+1], eq)
            i = i + 2
            sym_lst.remove('/')
            final *= eq

        if '*' in sym_lst:
            print("inside",i) 
            print(num_lst[i])
            print(num_lst[i+1])
            eq = num_lst[i] * num_lst[i+1]
            print(num_lst[i] , num_lst[i+1], eq)
            i = i + 2
            sym_lst.remove('*')
            final *= eq

            
    print(float(final))

bodmas()
# 2+2/2

