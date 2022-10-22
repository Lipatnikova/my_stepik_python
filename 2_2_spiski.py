from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/selects2.html'
    browser.get(link)

    time.sleep(3)

    # browser.find_element(By.TAG_NAME, "select").click()
    # browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    result = int(num1) + int(num2)
    result = str(result)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(result)

    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(5)
    browser.quit()
