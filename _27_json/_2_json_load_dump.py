import json

file = open("C:\\Users\\vashi\\OneDrive\\Documents\\DS291022B\\DS291022B\\Python\\_27_json\\demo.json")

# return the json object as a dictionary object
data = json.load(file)
print(data)
print(type(data))

file1 = open("C:\\Users\\vashi\\OneDrive\\Documents\\DS291022B\\DS291022B\\Python\\_27_json\\test.json","w")

# stores the dict object as json object
json.dump(data,file1)