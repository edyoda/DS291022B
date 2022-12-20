# array ---> list

# List 
# it accepts heterogenous data (only in python and js)
# it doesnot have a fix size (only in python and js)
# fetch the data
# insert the data
# delete the data
# update the data

# lst = [5,6,7,1,3,44]
# lst.append(8)
# lst.extend([25,7,4,567])
# lst.remove(3)
# print(lst)

class array:
    def __init__(self,fix_size):
        self.fix_size = fix_size
        self.data = []
        self.length = 0

    def add(self,element):
        if self.length < self.fix_size:
            self.data.append(element)
            self.length += 1
        else:
            print("Array is full")

    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Index out of range")
        else:
            del self.data[index]
            self.length -= 1

    def display(self):
        for i in range(self.length):
            print(self.data[i])

    def update(self,index,element):
        if index < 0 or index >= self.length:
            print("Index out of range")
        else:
            self.data[index] = element 

    def insert(self, index, element):
        if index < 0 or index > self.length:
            print("Index out of range")
        elif self.length == self.fix_size:
            print("Array is full")
        else:
            self.data.insert(index, element)
            self.length += 1

obj = array(3)
obj.add(10)
obj.add(20)
obj.add(30)
print(obj.data)

obj.remove(1)
print(obj.data)

obj.add(90)
print(obj.data)

obj.update(2,100)
print(obj.data)

obj.remove(0)
print(obj.data)

obj.insert(1,200)
print(obj.data)