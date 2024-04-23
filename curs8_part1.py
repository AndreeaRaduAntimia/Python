from selenium import webdriver
import time

# definirea driverului de Chrome (obiectului)
driver = webdriver.Chrome()

# deschiderea unei pagini web
driver.get("http://google.com")

# asteapta 5 secunde
time.sleep(5)

# inchiderea tabului curent
driver.close()

# sau
# inchiderea browserului cu totul
# driver.quit()
