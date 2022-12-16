from bs4 import BeautifulSoup   

file = open("C:\\Users\\vashi\\OneDrive\\Documents\\DS291022B\\DS291022B\\Python\\_28_xml\\demo.xml")

soup = BeautifulSoup(file,"html.parser")
# print(soup)

# it converts xml format into list object
data = soup.find_all("student")
# print(data)

# name = soup.find("name")
# print(name.text)

# rno = soup.find("rno")
# print(rno.text)

# for i in data:
#     print(i.find("name").text)

fav_student = soup.find("name",{"name":"fav"})
print(fav_student.text)