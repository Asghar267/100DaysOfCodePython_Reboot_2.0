import requests
from bs4 import BeautifulSoup
import re

url = "https://webscraper.io/test-sites/e-commerce/allinone"
req = requests.get(url)
print(req)

soup = BeautifulSoup(req.text, 'lxml')

tagdiv = soup.div # working with tag
# print(tagdiv)
tagheader = soup.header # working with tag
# print(tagheader)
atb =tagheader.attrs  # getting attribute in tag
print(atb)
# print(atb['class'])

#Navigable Strings
print("\n# Navigable Strings")
print(tagdiv.p)
print(tagdiv.p.string) # extracting text
print(tagdiv.ul.li.a) # #Navigating

#find function
print("\n find function")
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
req2 = requests.get(url)
soup = BeautifulSoup(req2.text, 'lxml')

print(soup.find("h4","price"))
# also we can do with multiple classes
print(soup.find("h4",{'class':"pull-right price"})) #finding class
print(soup.find("h4",{'class':"pull-right price"}).text) #also we can use string instaed text
print(soup.find("a",class_='title')) #also we can find like this
print(soup.find("p",class_="description").string)

# findall() Function with Tags and Attributes
print("\n findall() Function with Tags and Attributes")
print(soup.find_all("h4",class_="pull-right price"))
print(soup.find_all("h4",class_="pull-right price")[0].text)

# findall() Function with regex method
print("\n findall() Function with regex method")

print(soup.find_all(string= re.compile("Galaxy")))


#Extracting nested html tag
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

re = requests.get(url)
soup = BeautifulSoup(re.text, "lxml")

sidebar = soup.find("div", class_="col-md-3 sidebar")
print(sidebar.text)
print(sidebar.find("ul", id="side-menu").find_all("a"))
for i in sidebar.find("ul", id="side-menu").find_all("a"):
    print(i.text)




