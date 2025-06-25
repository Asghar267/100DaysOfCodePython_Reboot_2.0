import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen

# its working but only scraping 8 gigs

url = "https://www.fiverr.com/search/gigs?query=web%20scraper&source=top-bar&acmpl=1&search_in=everywhere&search-auto" \
      "complete-original-term=web%20s&search-autocomplete-available=true&search-autocomplete-type=suggest&search-autoco" \
      "mplete-position=3&ref_ctx_id=043958cc5f0d81f13b5f37656e756a9a"

req = Request(url,
     headers={'User-Agent': 'Mozilla/5.0'}
)
web_byte = urlopen(req).read()
# print(webpage)
re = requests.get(url)
print(re)
webpage = web_byte.decode('utf-8')
soup = BeautifulSoup(webpage, "html.parser")
snames, titles, ratings, prices = [], [], [], []
box = soup.find("div",class_="layout-row content-row")
cards = box.find_all("div",class_="gig-card-layout")
print(len(cards))
tt =""
for card in cards:
    sname = card.find("div",class_="seller-name-and-country").text
    title = card.find("h3").text
    rating = card.find("div",class_="rating-wrapper").text
    price = card.find("a",class_="price").text
    tt +=title+", "
    print(f"{sname} - {title} - {rating} - {price}")
    snames.append(sname), titles.append(title), ratings.append(rating), prices.append(price)

df = pd.DataFrame({"Saller Name":snames, "Gig Titles":titles, "Rating":ratings, "Price": prices})
df.to_csv("WebScraping_gigDetails.csv")

print(tt)