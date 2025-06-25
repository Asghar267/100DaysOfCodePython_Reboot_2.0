# scraping airbnb

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.airbnb.com/s/Middle-East/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=" \
      "one_week&price_filter_input_type=0&price_filter_num_nights=4&channel=EXPLORE&place_id=ChIJt_9CgWXEfhURLKdeISCDWwo&date_picker" \
      "_type=calendar&checkin=2023-04-17&checkout=2023-04-21&source=structured_search_input_header&search_type=user_map_move&query=Middl" \
      "e%20East&ne_lat=49.77493539631446&ne_lng=53.81787497942324&sw_lat=14.765405861087427&sw_lng=12.619144510673237&zoom=4&zoom_level=4" \
      "&search_by_map=true"

Names, Prices, Descriptions, Ratings = [], [], [], []

req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
for i in range(1,14):
      print(i)
      cards = soup.find_all("div", class_="c4mnd7m dir dir-ltr")

      next = soup.find("a",class_="l1j9v1wn c1ytbx3a dir dir-ltr").get("href")
      next_link = "https://www.airbnb.com/" + next
      print(next_link)

      req = requests.get(next_link)
      soup = BeautifulSoup(req.text, "lxml")

      for card in cards:
            name = card.find("div", class_="t1jojoys dir dir-ltr").text
            # print(name)  # title
            detail = card.find("div", class_="t1jojoys dir dir-ltr").text
            price = card.find("div", class_="p11pu8yw dir dir-ltr").text
            # print(price)
            detail = card.find("div", class_="nquyp1l s1cjsi4j dir dir-ltr").text
            # print(detail)
            rating = card.find("span", class_="t5eq1io r4a59j5 dir dir-ltr")
            if rating == None:
                  print("no ratings")
                  Ratings.append("No Ratings")
            else:
                  Ratings.append(rating.text)
                  # print(Ratings)

            Names.append(name)
            Descriptions.append(detail)
            Prices.append(price)

df = pd.DataFrame({"Names":Names, "Ratings":Ratings, "Prices":Prices,"Details":Descriptions})
df.to_csv("homes_data_Day25_6.csv")
