from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# definirea driverului de Chrome (obiectului)
driver = webdriver.Chrome()

driver.get("https://www.ebay.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".gh-td > div > button").click()

time.sleep(5)

# scroll in pagina
# metoda 1 de scroll down in pagina
driver.execute_script("window.scrollBy(0,2000)", "")

# metoda 2 de scroll
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "[data-sp='m571.l2895']").click()

url = driver.current_url
print(url)
assert "/help/account/default/" in url
