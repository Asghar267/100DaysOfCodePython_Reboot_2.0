#sele

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
s = Service("H:\\chromedriver.exe")

driver = webdriver.Chrome(service=s)

# driver.get("https://www.google.com/")
# driver.find_element_by_xpath("""/html/body/section[1]/div/div/div[2]/img""")
# time.sleep(3) # time to load page /
# # driver.find_element_by_xpath("""/html/body/section[1]/div/div/div[1]/div/div/button""").click() # for clicking on button wscube
# search = driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input""")
# search.send_keys("Asghar267")
# search.send_keys(Keys.ENTER)



#Scraping Scrooling web site

driver.get("https://www.ajio.com/men-footwear/c/830207?query=%3Arelevance%3Al1l3nestedcategory%3AMen%20-%20Formal%20Shoes&gridColumns=3")
time.sleep(4) # time to load page /

while True:
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == height: break
