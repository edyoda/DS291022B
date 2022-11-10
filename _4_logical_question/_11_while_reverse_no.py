no = int(input("Enter a num : "))

# 536
# 635
rev = 0

# mod = no % 10              # 6
# rev = rev * 10 + mod       # 6
# no = no // 10               # 53

# mod = no % 10              # 3
# rev = rev * 10 + mod       # 6 * 10 = 60 + 3 = 63
# no = no // 10               # 5

# mod = no % 10              # 5
# rev = rev * 10 + mod       # 635
# no = no // 10              # 0  

# print(rev)

while no != 0:
    mod = no % 10              
    rev = rev * 10 + mod       
    no = no // 10              

print(rev)