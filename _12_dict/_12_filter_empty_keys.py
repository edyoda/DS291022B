dict_demo = {'a':10,'b':90,'c':100,'d':None}

new_dict = {}
for k in dict_demo.keys():
    if dict_demo[k] != None:
        new_dict[k] = dict_demo[k]

print(new_dict)