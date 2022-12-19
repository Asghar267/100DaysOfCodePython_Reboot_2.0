from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

lang = driver.find_element(By.ID, "langSelect-EN")
lang.click()

driver.implicitly_wait(10)
cookies = driver.find_element(By.ID, "bigCookie")
count_cookies = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice"+str(i)) for i in range(1, -1,-1)]

# actions = ActionChains(driver)
# actions.click(cookies)

for i in range(200000):
    count_cookies = driver.find_element(By.ID, "cookies")
    cookies.click()
    count = int(count_cookies.text.split(" ")[0])

    print(count)
    # sleep(0.5)
    # actions.perform()
    for item in items:
        value =  int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
