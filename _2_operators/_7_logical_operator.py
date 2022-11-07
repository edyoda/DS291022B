# Logical Operator
# and  - returns True when all the conditions are True
# or   - returns True when atleast one conditions is True
# not  - will revert the output

no1 = 90
no2 = 78

and_demo = no1 > no2 and no1 != 90
print("And : ",and_demo)

or_demo = no1 > no2 or no1 != 90
print("And : ",or_demo)

not_demo = not(no1 > no2)
print("Not : ",not_demo)