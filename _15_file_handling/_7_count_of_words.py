file = open("edyoda.txt","r")
count = 0
for i in file:
    words = i.split()
    count += len(words)
    
print(count)