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

def reverse_stack(stack):
    reversed_stack = Stack()
    while not stack.is_empty():
        reversed_stack.push(stack.dequeue())
    return reversed_stack


data = input("Enter the values for the stack,add with d hspaces: ")


stack = Stack()
for item in data.split():
    stack.push(item)

stack.display().sort()
print(stack.display())


reversed_stack = reverse_stack(stack)
while not reversed_stack.is_empty():
    print("here is reveresed values:- ",reversed_stack.pop())



# class Stack:

# 	def __init__(self):
# 		self.Elements = []
		
# 	def push(self, value):
# 		self.Elements.append(value)
	
# 	def pop(self):
# 		return self.Elements.pop()
	
# 	def empty(self):
# 		return self.Elements == []
	
# 	def show(self):
# 		for value in reversed(self.Elements):
# 			print(value)

# def BottomInsert(s, value):

# 	if s.empty():
# 		s.push(value)
		
# 	else:
# 		popped = s.pop()
# 		BottomInsert(s, value)
# 		s.push(popped)

# def Reverse(s):
# 	if s.empty():
# 		pass
# 	else:
# 		popped = s.pop()
# 		Reverse(s)
# 		BottomInsert(s, popped)
# stk = Stack()

# stk.push(8)
# stk.push(9)
# stk.push(1)
# stk.push(4)
# stk.push(8)
# stk.push(5)

# print("Original Stack")
# stk.show()
 
# print("\nStack after Reversing")
# Reverse(stk)
# stk.show()



