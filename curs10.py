from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

# definirea driverului de Chrome (obiectului)
driver = webdriver.Chrome()

driver.get("https://carturesti.ro")
driver.maximize_window()

allow_cookies = driver.find_elements(By.XPATH, "//*[contains(text(),'Permite doar esențiale')]")
allow_cookies[0].click()

element = driver.find_element(By.XPATH, "//*[contains(text(),'Comandă-l aici')]")

actions = ActionChains(driver)
actions.move_to_element(element).perform()

element.click()

time.sleep(5)

url = driver.current_url
print(url)
assert "coupon-checkout" in url

# verificam cate elemente de tip input sunt in pagina
# input_boxes = driver.find_elements(By.XPATH, "//input")  # not reliable in cazul nostru
input_boxes = driver.find_elements(By.CSS_SELECTOR, ".form-control")

print("Sunt", len(input_boxes), "inputuri")

assert len(input_boxes) == 1

driver.find_element(By.XPATH, "//a[contains(text(),'Akissa Saike')]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[contains(text(),'Ghost Reaper Girl - Volume 4')]").click()

for i in range(5):
    driver.find_element(By.ID, "cartu-add-to-cart-btn-x").click()
    time.sleep(3)

time.sleep(2)

cart_elements_count = driver.find_element(By.XPATH, "//span[@data-ng-bind='cart.count()']").text
print(cart_elements_count)

assert cart_elements_count == "5"

