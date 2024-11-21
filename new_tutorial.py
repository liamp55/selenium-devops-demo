from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

print(driver.title)

search = driver.find_element(By.NAME, "search")
search.send_keys("hello")
search.send_keys(Keys.RETURN)

link = driver.find_element(By.LINK_TEXT, "Germanic languages")
link.click()



main = driver.find_element(By.CLASS_NAME, "mw-page-container")
print(main.text)

time.sleep(5)
driver.quit()
