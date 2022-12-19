# web scraping
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.techwithtim.net")
print(driver.title)

search = driver.find_element(By.NAME,"s")
search.send_keys("test")
search.send_keys(Keys.RETURN) # Return means enter
# print(driver.page_source)
try:
    main = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements(By.TAG_NAME ,"article")
    for article in articles:
        header = article.find_elements(By.CLASS_NAME ,"entry-summary")
        for eachItem in header:
            print(eachItem.text)
finally:
    driver.quit()


# main = driver.find_element("id","main")
# print(main.text)
# time.sleep(5)
# driver.close() # close tab
# driver.quit() # close browser