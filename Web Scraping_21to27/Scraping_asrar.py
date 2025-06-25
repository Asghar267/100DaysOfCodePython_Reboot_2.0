# in this code I will Scrape Asrar youtube channel

import requests
from bs4 import BeautifulSoup
url = "https://www.youtube.com/watch?v=Xwv9dkl00U4&list=UULFBfUmyIysxBYp-YASjRBJUw"
request = requests.get(url)
print(request)

page = request.content
# print(page)
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()
# print(soup)
# titl = soup.findAll("style-scope")
# t = soup.find_all(class_="yt-simple-endpoint style-scope ytd-grid-video-renderer")
# print(titl)
# print(t)
print(soup.find('p'))