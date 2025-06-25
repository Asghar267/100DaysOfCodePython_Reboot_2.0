import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://purpleleafshop.com/"

url1 = "https://purpleleafshop.com/collections/patio-umbrella"
# url2 = "https://purpleleafshop.com/collections/hardtop-gazebo"

Title, Prices, Ratings, Size = [], [], [],[]

req = requests.get(url1)
soup = BeautifulSoup(req.text, "lxml")

cards = soup.find_all("div", class_="product-item product-item--vertical 1/3--tablet 1/3--lap-and-up")
# print(cards)
# links = cards.find_all("a")
# print(links)
print(len(cards))
i = 1
for card in cards:
    print(i)
    links = "https://purpleleafshop.com/"+card.find("a").get("href")
    # reql = requests.get(links)
    # soups = BeautifulSoup(req.text, "lxml")

    # print(cards.text)
    print(links)
    preq = requests.get(links)

    product = BeautifulSoup(preq.text, "lxml")

    # card = product.find("div", class_="card__section")
    # meta = card.find("div", class_="product-meta")
    meta = product.find("div", class_="product-meta")

    title = meta.find("h1").text
    Title.append(title)
    print(meta.find("h1").text)
    # print(meta.find("div", class_="review-widget").text)
    # for i in meta.find("div", class_="review-widget").text:
    #     print(i)

    # print(meta.find("div", class_="ryviu-item product-widget__ryviut").string)
    # print(meta.find("div", class_="ryviu-item product-widget__ryviut").text)
    # print("rating :",meta.find("div",class_="ryviu-number-widget").string)
    # s = meta.find("div",class_="ryviu-number-widget")

    # finding and scraping review and rating
    s = meta.find("div",class_="review-widget")
    ss = str(s).split()
    # print(ss)
    review_rating =  ss[5].split('"')
    print("Rating : ",review_rating[1])
    Ratings.append(review_rating[1])
    try:
        siz = product.find("div", class_="block-swatch").text
        print("size: ",siz.strip())
        Size.append(siz.strip())
    except:
        Size.append("None")
        pass
    p = product.find("span", class_="price price--highlight").text
    print("price: ",p)
    Prices.append(p)
    i += 1
df = pd.DataFrame({"title":Title, "Price":Prices, "Ratings":Ratings,"Size":Size})
print(Title)
print(Ratings)
print(Prices)
print(Size)
df.to_csv("products.csv")