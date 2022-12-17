# deque

# it is open from both the ends
# you can add/delete the elements from both the ends
# queue - FIFO --> lst

from collections import deque

obj = deque([1,2,3,4,5])

print(obj)

obj.append(10)
print(obj)

obj.appendleft(100)
print(obj)

obj.pop()
print(obj)

obj.popleft()
print(obj)