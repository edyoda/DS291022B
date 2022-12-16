import csv

column = ["rno","name"]
rows=[[1,"Raj"],[2,"Ram"]]

with open("C:\\Users\\vashi\\OneDrive\\Documents\\DS291022B\\DS291022B\\Python\\_26_csv\\test.csv","w") as file:
    writer = csv.writer(file)

    writer.writerow(column)
    writer.writerows(rows)