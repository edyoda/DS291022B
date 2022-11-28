lst=[1,2,3,4,5,6,7,8,9]
#o/p:["odd","even",....]

result=list(map(lambda data: "Even" if data%2==0 else "Odd",lst))
print(result)
