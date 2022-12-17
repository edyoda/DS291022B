import requests

# url = "https://reqres.in/api/users"

# data = {
#     "name": "bharati",
#     "job": "developer"
# }

# # response = requests.post(url,json=data).json()
# # print(response)

# response = requests.request('POST',url,json=data).json()
# print(response)



url = "http://127.0.0.1:5000/edyoda"

data = {"naam":"Bharati"}

response = requests.post(url,params=data) # json,data,params
print(response.json())
