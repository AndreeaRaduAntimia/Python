import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver.maximize_window()

option = Options()

option.add_argument("start-maximized")
option.add_argument("--disable-notifications")

driver = webdriver.Chrome(option)
# driver.get("https://www.elefant.ro/")
# sleep(5)
#
# driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
# sleep(5)
#
# search_input_list = driver.find_elements(By.NAME, "SearchTerm")
# search_input_list[0].click()
#
# search_input_list[0].send_keys("Iphone 14")
#
# search_input_list[0].send_keys(Keys.ENTER)
#
# sleep(5)
#
# # sau
# # search_buttons_list = driver.find_elements(By.XPATH, "//button[@name='search']")
# # search_buttons_list[0].click()
#
# results_list = driver.find_elements(By.CSS_SELECTOR, "[class='product-title']")
# assert len(results_list) >= 10
#
# prices_list = driver.find_elements(By.CSS_SELECTOR, ".current-price")
# prices_list_text = []
#
# for price in prices_list:
#     if price.text != "N/A":
#         prices_list_text.append(price.text)
#
# print(prices_list_text)
#
# prices_list_integer_part = []
# # extragem tot pana la virgula din string
# # for price_text in prices_list_text:
# #     prices_list_integer_part.append(int(price_text.split(",")[0]))
# #
# # print(prices_list_integer_part)
# #
# # lowest_price_element = min(prices_list_integer_part)
# #
# # assert lowest_price_element == 7
#
# # cazul in care am avea 2 parti intregi egale
# prices_list_float = []
#
# for price_text in prices_list_text:
#     prices_list_good = price_text.replace(",", ".")
#     prices_list_float.append(float(prices_list_good.split(" ")[0]))
#
# print(prices_list_float)
# print(sorted(prices_list_float))
#
# assert min(prices_list_float) == 7.99
#
# assert driver.title == "Cauti Iphone 14? - Vino pe Elefant.ro!"

driver.get("https://www.elefant.ro/")
sleep(5)

driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
sleep(5)

driver.find_element(By.CSS_SELECTOR, ".js-login-prompt").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#account-layer > .my-account-login").click()
sleep(2)

email_input = driver.find_element(By.NAME, "ShopLoginForm_Login")
email_input.send_keys("test@google.com")

password_input = driver.find_element(By.NAME, "ShopLoginForm_Password")
password_input.send_keys("test")

connect_button = driver.find_element(By.NAME, "login")
connect_button.click()

alert_message = driver.find_element(By.CSS_SELECTOR, ".alert").text

assert alert_message == "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."

assert "ViewUserAccount-ProcessLogin" in driver.current_url

# workaround problema selenium stale element not found
driver.find_element(By.NAME, "ShopLoginForm_Login").clear()
driver.find_element(By.NAME, "ShopLoginForm_Login").send_keys("test")
sleep(4)

field_error_message_validation = driver.find_element(By.CSS_SELECTOR, "[data-bv-validator='emailAddress']").text
assert field_error_message_validation == "Te rugăm să introduci o adresă de e-mail validă."

assert driver.find_element(By.NAME, "login").is_enabled() is False
