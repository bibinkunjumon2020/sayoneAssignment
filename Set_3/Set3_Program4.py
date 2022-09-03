"""

Fetch data from the URL https://www.w3schools.com/xml/simple.xml and print name, price of each item.

"""
import requests
from bs4 import BeautifulSoup



response = requests.get("https://www.w3schools.com/xml/simple.xml")

soup = BeautifulSoup(response.content,features='lxml')
print(soup)

name = soup.find_all("name")
print("----------",name)
price = soup.find_all("price")
print("----------",price)
data ={}
for ele in range(0,len(name)):
    data[name[ele].getText()]=price[ele].getText()

print("--------------FINAL NAME AND PRICE LIST")
print(data)