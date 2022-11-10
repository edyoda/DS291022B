num = 3452
count = 0

while num != 0:
    num //= 10  # 0
    count += 1  # 4
    print(num , count)


print("Number of digits: ",count)
