
"""

Fetch image url, country name from the URL http://example.webscraping.com/ using beautifulsoup
"""

import requests
from bs4 import BeautifulSoup


url = "http://example.webscraping.com/"
response = requests.get(url)
print("response----",response)
soup = BeautifulSoup(response.text, "html.parser")
#print("soup---",soup)
image_links = soup.find_all("img")
print(image_links)


image_data = []

for link in image_links:
    image_tag = link.findChildren("img")
    image_data.append(link.get('src'))
print("All Image data are :\n")
print(image_data)
