from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# definirea driverului de Chrome (obiectului)
driver = webdriver.Chrome()

driver.get("https://fs2.formsite.com/meherpavan/form2/")

# maximizarea ferestrei(tabului)
driver.maximize_window()

# accesarea paginii anterioare
driver.back()

time.sleep(5)

driver.forward()
time.sleep(5)

# print(driver.title)
assert driver.title == "Selenium Practice Form"

# introducere valori in text boxuri
driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Razvan")

text_box_2 = driver.find_element(By.ID, "RESULT_TextField-2")
text_box_2.send_keys("Corjos")
time.sleep(2)

text_box3 = driver.find_element(By.NAME, "RESULT_TextField-3")
text_box3.send_keys("+4075355245262")
#
# faceti voi inputul pentru celelalte campuri: country, city, email address dupa model
# TODO

status_element_email = driver.find_element(By.ID, "RESULT_TextField-6").is_displayed()
print("Este afisat", status_element_email)  # true/false

# testul automat efectiv
assert status_element_email == True  # test pozitiv
assert status_element_email != False  # test negativ

first_gender_element_status = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()
print("Este selectat genul masculin", first_gender_element_status)

assert first_gender_element_status != True  # test negativ
assert first_gender_element_status == False  # test negativ

time.sleep(5)

radio_gender_male = driver.find_element(By.CSS_SELECTOR, "td > [for='RESULT_RadioButton-7_0']")
radio_gender_male.click()

phone_label_text = driver.find_element(By.CSS_SELECTOR, "#q9 > [for='RESULT_TextField-3']").text
print(phone_label_text)

assert phone_label_text == "Phone"

male_text_label = driver.find_element(By.CSS_SELECTOR,
                                      "#q26 > table > tbody > tr > td > [for='RESULT_RadioButton-7_0']").text
print(male_text_label)
assert "Male" in male_text_label
time.sleep(5)


checkbox_monday_label = driver.find_element(By.CSS_SELECTOR, "td > [for='RESULT_CheckBox-8_1']")
checkbox_monday_label.click()

checkbox_sunday_label = driver.find_element(By.CSS_SELECTOR, "td > [for='RESULT_CheckBox-8_0']")
checkbox_sunday_label.click()
time.sleep(5)

# verificare daca primul checkbox este bifat
checkbox_monday = driver.find_element(By.ID, "RESULT_CheckBox-8_0")

assert checkbox_monday.is_selected()

# selectare elemente din dropdown
# metoda 1

element = driver.find_element(By.ID, "RESULT_RadioButton-9")
dropdown = Select(element)

time.sleep(2)
dropdown.select_by_visible_text("Afternoon")
time.sleep(2)
dropdown.select_by_value("Radio-2")
time.sleep(2)
dropdown.select_by_index(1)
time.sleep(2)

# metoda 2
element.click()
chosen_option = driver.find_element(By.CSS_SELECTOR, "#RESULT_RadioButton-9 > option:nth-child(3)")
chosen_option.click()
time.sleep(2)

# afisam textul din fiecare option din dropdown
all_options = dropdown.options

for option in all_options:
    print(option.text)


