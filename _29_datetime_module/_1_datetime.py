# datetime module - helps to code wrt to date and time


import datetime as dt

current_date = dt.datetime.now()
print(current_date)

print("A : ",current_date.strftime("%A"))

print("a : ",current_date.strftime("%a"))

print("B : ",current_date.strftime("%B"))

print("b : ",current_date.strftime("%b"))

print("C : ",current_date.strftime("%C"))

# month = current_date.month
# print(month)

# year = current_date.year
# print(year)

# day = current_date.day
# print(day)

# hr = current_date.hour
# print(hr)

# mins = current_date.minute
# print(mins)

# secs = current_date.second
# print(secs)

# ms = current_date.microsecond
# print(ms)