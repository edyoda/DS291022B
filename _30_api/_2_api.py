import requests

# url = "https://catfact.ninja/fact"
url = "https://reqres.in/api/users?page=2"



# response = requests.request('GET',url).json()
# print(response)


response = requests.get(url).json()
print(response)

