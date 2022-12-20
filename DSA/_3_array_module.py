import array as arr

# you can only add homogenous datatype
data = arr.array('i',[1,3,4,1,54,6,67])
print(data)

data.append(89)
print(data)

data.pop()
print(data)

data.extend([4,5,3,21])
print(data)