import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://ticker.finology.in/"
r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text, "lxml")

tabel = soup.find("table", class_="table table-sm table-hover screenertable")
# print(tabel.text)

theader = tabel.find_all("th")
titles= [theader[0].text, theader[1].text, theader[2].text]
# print(titles)
df = pd.DataFrame(columns=titles)

for c ,row in enumerate (tabel.find_all("tr")[1:]):
    # print(row)
     # print(row.find_all("td"))
    th = [i.text for i in row.find_all("td")]
    # print(th)
    # print(len(th))
    # df.append([th[0].text,th[1].text,th[2].text])
    df.loc[c]=([i.text for i in row.find_all("td")])

print(df)