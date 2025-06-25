# Scraping Multiple Pages on Websites
import pandas as pd
import requests
from bs4 import BeautifulSoup

title = []
description = []
categories = []
price = []
rating = []
for i in range(1, 11): #page nation
    url = "https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&ctx=eyJjYXJk" \
          "Q29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJ" \
          "VExFIiwidmFsdWVzIjpbIkxhdGVzdCBTYW1zdW5nIG1vYmlsZXMgIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBT" \
          "FVFRCJ9fX19fQ%3D%3D&wid=1.productCard.PMU_V2_1&page=" +str(i)

    req = requests.get(url)
    print(req)
    soup = BeautifulSoup(req.text, "lxml")
    print(soup)
    # print(soup.find("a",class_="_1LKTO3").get("href")) # geting href link on next button
    # nextpage = soup.find("a",class_="_1LKTO3").get("href")

    # box = soup.find("div", class_="_1YokD2 _3Mn1Gg")  # Box of all cards
    cards = soup.find_all("div", class_="_3pLy-c row")  # getting all cards in box
    print(len(cards))

    for card in cards:
        title.append(card.find("div", class_="_4rR01T").text)
        description.append(card.find("ul", class_="_1xgFaf").text)
        price.append(card.find("div", class_="_3tbKJL").text)
        previews = card.find("div", class_="_3LWZlK")

        if previews == None:
            print("no ratings")
            rating.append("No Ratings")
        else:
            rating.append(previews.text)
    print(len(title))
    df = pd.DataFrame({"Title": title, "Price": price, "Rating": rating, "Description": description})

print(df)
df.to_csv("flipkart_phone.csv")
