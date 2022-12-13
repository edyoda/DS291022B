# ### Exception Handling
# # lst = [5,6,4]
# # print(lst[4])

# lst = [5,6,4]
# try:
#   print(lst[4])
# except:
#     # print("Try another list lenght more then 4 ")
#     # size = int(input("Enter the lenght of the list = "))
#     # lst=[]
#     # for i in range(size):
#     #   element = int(input("Enter the element you want in the list = "))
#     #   lst.append(element)
#     # #   lst.sort()
#     #   print(lst)

#     print("Enter the index between 0 - ",len(lst)-1)
#     index = int(input())
#     print(lst[index])


      
try:
    lst = [5,6,4]
    print(lst[4])
except Exception as ex:
    print("Exception Error: ", ex)
    print("try other list")
    try:
        size = int(input("enter size of list: "))
        lst = []
        for i in range(size):
            object = int(input("enter objects "))
            lst.append(object)
        print(lst[4])
    except Exception as ex:
        print("Again given list is out of range")
    print("End of program")
