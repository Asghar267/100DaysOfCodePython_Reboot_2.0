from time import sleep
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

title, link, compare_price, price_on_sale, desc, imgs = [], [], [], [], [], []

def scrape(i):
    url = "https://krazymarts.com" + i.get("href")
    print("https://krazymarts.com" + i.get("href"))
    link.append(url.strip())
    req = requests.get(url)
    soup2 = BeautifulSoup(req.text, 'lxml')
    defa = soup2.find("div", class_="halo-product-content")
    card = defa.find("div", class_="col-md-6 product-shop")
    title.append(card.find("h1", {'class': "product-title"}).text.strip())
    compare_price_element = card.find("span", class_="compare-price")
    compare_price.append(compare_price_element.text.strip() if compare_price_element else "nn")
    psale = card.find("span", class_="price on-sale")
    price_on_sale.append(psale.text.strip() if psale else "nn")
    desc.append(str(card.find("div", class_="tab-content").text.strip()))
    imgs.append("https://" + str(soup2.find("a", class_="fancybox").get("href")).strip())


def saving_fil_nan():
    # Assuming title, compare_price, price_on_sale, desc, link, and imgs are your lists
    max_length = max(len(title), len(compare_price), len(price_on_sale), len(desc), len(link), len(imgs))
    # Fill missing values in shorter lists with np.nan
    title.extend([np.nan] * (max_length - len(title)))
    compare_price.extend([np.nan] * (max_length - len(compare_price)))
    price_on_sale.extend([np.nan] * (max_length - len(price_on_sale)))
    desc.extend([np.nan] * (max_length - len(desc)))
    link.extend([np.nan] * (max_length - len(link)))
    imgs.extend([np.nan] * (max_length - len(imgs)))

    df = pd.DataFrame(
        {"Title": title, "compare_price": compare_price, "price_on_sale": price_on_sale, "desc": desc,
         "Link": link, "Imags": imgs})
    df.to_csv("home_products.csv")

driver = webdriver.Chrome()
# Open a web page

driver.get("https://krazymarts.com/collections/home-acessories")
# Get the initial page height
initial_height = driver.execute_script("return document.body.scrollHeight")
sleep(3)
for i in range(36):
    print("scroll :", i)
    sleep(2)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
updated_html = driver.page_source
driver.quit()
soup = BeautifulSoup(updated_html, 'html.parser')
links = set(soup.findAll("a", class_="product-title"))

print("total products: ", len(links))
break_interval = 10
for count, i in enumerate(links):
    sleep(2)
    try:
        if count % break_interval == 0:
            print(count, " Taking a 10-second break...", count % break_interval)
            sleep(5)  # Sleep for 10 seconds
        print("count: ", count)
        scrape(i)
    except:
        print("in Except block")
        try:
            sleep(10)
            print("int try count: ", count)
            scrape(i)
        except:
            print("in Except block 2")
            print("failed in try count no: ", count)
            saving_fil_nan()

saving_fil_nan()





