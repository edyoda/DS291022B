class node:
    def __init__(self,data,link=None):
        self.data = data # element
        self.link = link # memory location of the previous node

class linkedlist:
    def __init__(self,head=None):
        self.head = head

    def append(self,data):
        new_node = node(data,self.head)
        self.head = new_node

    def display(self):
        itr = self.head
        while itr:
            print(itr.data,"------>",itr.link)
            itr = itr.link

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def size(self):
        count = 0
        itr = self.head
        while itr:
            count += 1 
            itr = itr.link
        return count

    def remove(self,index):  # 2
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:   
                print("Element which has the memory location of the element present on the that index : ",itr.data)
                print("Before modifying the addres : ",itr.link)              
                itr.link = itr.link.link # 1003 = 1004
                print("After modifying the address : ",itr.link) 
            itr = itr.link
            count += 1 
            
    # 10 - 1001
    # 20 - 1002
    # 30 - 1003 # 2
    # 40 - 1004 # 3
    # 50 - 1005


obj = linkedlist()
obj.append(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.append(50)

obj.display()
print()
# print(obj.isEmpty())

# print(obj.size())
print()
obj.remove(2)
print()
obj.display()