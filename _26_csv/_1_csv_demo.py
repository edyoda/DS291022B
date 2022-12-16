# CSV
# Comma Seperated Value
# extension .csv
# all the data in this file are seperated by comma

import csv

rows = []
with open("C:\\Users\\vashi\\OneDrive\\Documents\\DS291022B\\DS291022B\\Python\\_26_csv\\demo.csv") as file:
    data = csv.reader(file)

    header = next(data)
    print(header)

    print()

    for row in data:
        rows.append(row)

    print(rows)        

    for i in rows[:2]:
        print(i)

    count = data.line_num
    print("Row Count : ",count)

