# Queue

# FIFO - First in First out

class queue:
    def __init__(self):
        self.data = []

    # adding the data
    def enqueue(self, element):
        self.data.append(element)

    # removing first element
    def dequeue(self):
        if not self.isEmpty():
            return self.data.pop(0)
        else:
            return None
        

    # return first element
    def front(self):
        if not self.isEmpty():
            return self.data[0]
        else:
            return None
    
    # return last element
    def rear(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return None

    def display(self):
        print(self.data)

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

queue = queue()

queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)

queue.display()

# queue.dequeue()

# queue.display()

print(queue.front())
print(queue.rear())

print(queue.isEmpty())

print(queue.size())