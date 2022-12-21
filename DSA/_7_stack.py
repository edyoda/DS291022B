# stack

# LIFO - Last in first out
# push - adding the element
# pop  - removing the last element and also return the last element
# peek - displaying the last element

from collections import deque

class stack:
    def __init__(self):
        self.data = deque()

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def display(self):
        return self.data

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size == 0

stack = stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.display()  

# print(stack.pop())  
# stack.display() 

print(stack.peek())  

# stack.display() 

print(stack.size()) 
print(stack.isEmpty())
