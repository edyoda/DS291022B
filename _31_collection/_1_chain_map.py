# ChainMap
# used to combine multiple dictionary together
# it returns the list of dict

from collections import ChainMap

dict1 = {"a":"A","b":"B"}
dict2 = {1:"One",2:"Two"}
dict3 = {"rno":1,"name":"Bharati"}

chain_map = ChainMap(dict1,dict2,dict3)
print(chain_map)

print(chain_map["name"])

dict4 = {"z":"Z"}

chain_map = chain_map.new_child(dict4)
print(chain_map)
