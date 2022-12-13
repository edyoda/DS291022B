
### Exception
# str1 = None
# print("Length : ",len(str1))

### Exception Handling
# try:
#     str1 = None
#     print("Length : ",len(str1))
# except Exception as ex:
#     print("Input string is 'None' which has no length.",ex)
# print("End of program")


try:
  str1 = None
  print("Length : ",len(str1))
except:
  print("Initialize some other value")
  str1 = input("Enter the value")
  print("Length : ",len(str1))
