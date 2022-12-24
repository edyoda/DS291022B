# Time Complexity
# time taken by program to get executed

# lst = [6,19,30,16,4,12,14,67,89,90]
# Best Case = lst[0]
# Average Case = 6 iteration
# Worst Case = 10 iteration

# f(n) = 2n^2 + 3n + 1

# drop lower order values/term
# drop all the constant values

# n^2 => O(n^2)


########################################

# Loop

n = 10
a = 10
b = 20
sum = 0
for i in range(n):
    sum = a+b           # constant_time = c(n)  
                        #               = O(n) # called as Big O of (n)


########################################

# Nested Loop

for i in range(n):           # n = 5
    for j in range(n):       # n = 10
        sum = a+b            # constant_time = c(n^2)
                             #               = O(n^2)


########################################

# Sequential Statements

sum = a+b                              # c1           = O(1)

for i in range(n):                     # c2(n)
    sum = a+b

for j in range(n):                     # c2(n)
    sum = a+b

# c1+c2n+c3n  = O(n)


##########################################

# if else statement

# if condition:
#     # body         # O(n)
# else:
#     # body         # O(n^2)               = O(n^2)


# O(1) < O(n) < O(n^2)


# O(1) - Constant Time Complexity
# O(n) - Linear Time Complexity
# O(n2) - Quadratic Time Complexity
# O(logn) - Logarithmic Time Complexity

# Space Complexity

a = 10
b = 20
c = 30
sum = 0
def add():
    sum = a + b + c
    return sum

# 4 bytes

# 4 * 4 + 4
# 20 bytes

