import json

json_obj = """{
    "name":"Bharati",
    "female":true,
    "qualification":null,
    "designer":false
}"""

# converting json obj into dict obj
dict_obj = json.loads(json_obj)
print(dict_obj)
print(type(dict_obj))

dict_obj = {
    "rno":1,
    "name":"Bharati",
    "female":True
}

# converting dict obj into json obj
json_obj = json.dumps(dict_obj)
print(json_obj)
