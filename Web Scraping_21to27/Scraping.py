import requests
from bs4 import BeautifulSoup


url = "https://www.codewithharry.com/"

r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)

soup = BeautifulSoup(htmlcontent, "html.parser")

# print(soup.prettify())
title = soup.title
print(title.string)

# getting paragraphs
paras = soup.findAll('p')
# print(paras)
para = soup.find('p')
print(para)

print(soup.find('p')['class'])

# find all elements with class mt-2
print(soup.find_all("p", class_="mt-2"))
print()
print(soup.find('p').get_text())
# print("\n", soup.get_text()) # getting all text in page

# getting anchor tags
anchor = soup.findAll('a')
# print(anchor)
for link in anchor:
    print("href="+link.get('href'))


