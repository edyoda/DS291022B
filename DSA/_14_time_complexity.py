# Asymptotic Notation

# 1. Big O
# 2. Big Omega
# 3. Big Theta

# 1. Big O - worst case - upper bond
# lst = [6,19,30,16,4,12,14,67,89,90]


# f(n) <= c.g(n) => f(n) = O(g(n))
# n >= n0
# n0 >= 1

# n => input
# f(n) => function/method/single line statement
# c => constant value (which is used to satisfy the equation)
# g(n) => time complexity (worst)
# t => time taken
# n0 => threshold, beyond which no matter what input is given, it will not go beyond upper bond



# 2. Big Omega - lower bond (best case)
# lst = [6,19,30,16,4,12,14,67,89,90]

# f(n) >= c.g(n) => f(n) = Ω(g(1))
# n >= n0
# n0 >= 1


# 3. Big Theta - in between lower and upper bond (average case)
# lst = [6,19,30,16,4,12,14,67,89,90]

# c1.g(n) >= f(n) >= c2.g(n)
# n >= n0
# n0 >= 1