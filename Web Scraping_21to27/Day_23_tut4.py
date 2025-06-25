# scraping ipl 2022 acution data

import requests
from bs4 import BeautifulSoup
import pandas as pd

# IPL_teamsDAta = pd.

url = "https://www.iplt20.com/auction"
re = requests.get(url)
soup = BeautifulSoup(re.text, "lxml")

table = soup.find("table",class_="ih-td-tab auction-tbl")
trow = table.find("tr", class_="ih-pt-tbl")
titles = [t.text for t in trow.find_all("th")]
print(titles)
df = pd.DataFrame(columns=titles)


trow = table.find_all("tr")
td = table.find_all("tr")
for t in trow[1:]:
    print("")
    row = [r.string or r.find("h2",class_="ih-pt-cont").string for r in t.find_all("td")]
    df.loc[len(df)] = row
    print(row)

df.to_csv("ipl_AcutionData.csv")


