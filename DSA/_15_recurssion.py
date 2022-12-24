# 5! = 5 * 4 * 3 * 2 * 1

num = 5
fact = 1
for i in range(1,num+1):
    fact = fact * i

print(fact)

# 1 * 1 = 1
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * factorial(n-1)) 
    
print(factorial(num))

# 5 * factorial(4) 
# 4 * factorial(3)
# 3 * factorial(2)
# 2 * factorial(1)

