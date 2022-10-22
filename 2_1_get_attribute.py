from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CLASS_NAME, 'btn').click()

    # people_radio = browser.find_element(By.ID, "peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    #
    # assert people_checked is not None, "People radio is not selected by default"
    #
    # assert people_checked == "true", "People radio is not selected by default"
    #
    # robots_radio = browser.find_element(By.ID, "robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None


finally:
    time.sleep(10)
    browser.quit()
