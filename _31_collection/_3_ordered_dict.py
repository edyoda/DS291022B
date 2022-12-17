# OrderedDict

# it's a child class of dict class
# it remembers the order in which the key was inserted

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["a"] = "A"
ordered_dict["b"] = "B"
ordered_dict["c"] = "C"

print(ordered_dict)

print(ordered_dict["c"])