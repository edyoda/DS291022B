num=int(input("Enter a number to check whether palindrome : "))
og = num
rev= 0

while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

if rev == og:
    print ("Palindrome")
else: 
    print("Not palindrome")

# 123
# 1+2+3 = 6