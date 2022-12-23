class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def dequeue(self):
        return self.items.pop(0)

    def display(self):
        return self.items


data = input("Enter the values for the stack,add with d hspaces: ")

stack = Stack()
for item in data.split():
    stack.push(item)

stack.display().sort()
print(stack.display())


