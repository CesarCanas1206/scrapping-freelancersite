from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from login import *

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# driver.maximize_window()

# Open the freelancer.com website
driver.get("https://www.freelancer.com/")

desplayLogin(driver)

# Hover find job using ActionChains
hoverable1 = driver.find_element(By.PARTIAL_LINK_TEXT, "Find Jobs")
# hoverable.click()

ActionChains(driver).move_to_element(hoverable1).perform()
time.sleep(2)

hoverable2 = driver.find_element(By.PARTIAL_LINK_TEXT, "By Skill")
ActionChains(driver).move_to_element(hoverable2).perform()
time.sleep(5)

# Close the browser
driver.quit()
