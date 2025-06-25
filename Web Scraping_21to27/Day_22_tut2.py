import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

re = requests.get(url)
soup = BeautifulSoup(re.text, "lxml")

price=[]
title =[]
description = []
reviews = []

# print(soup.find('div',class_="col-sm-4 col-lg-4 col-md-4"))
alldivs = soup.find_all('div',class_="col-sm-4 col-lg-4 col-md-4")
for div in alldivs:
    # print(div.find('h4',class_="pull-right").text,end="")
    price.append(div.find('h4',class_="pull-right").text)
    title.append(div.find('a',class_="title").text)
    description.append(div.find('p',class_="description").text)
    reviews.append(div.find('p',class_="pull-right").text)
    # print("\n")

print(price)
print(title)
print(description)
print(reviews)

df = pd.DataFrame({"Product_name":title, "Price":price, "Description":description, "reviews":reviews})
print(df)
df.to_csv("Product_details.csv")




