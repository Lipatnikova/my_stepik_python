'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
browser.quit()
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
btn = browser.find_element(By.ID, 'book')
btn.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

input_value = browser.find_element(By.ID, 'input_value')
browser.execute_script("return arguments[0].scrollIntoView(true);", input_value)

x = browser.find_element(By.ID, 'input_value').text
x = calc(x)

answer = browser.find_element(By.ID, 'answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
browser.find_element(By.ID, 'answer').send_keys(x)

solve = browser.find_element(By.ID, 'solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", solve)
browser.find_element(By.ID, 'solve').click()

time.sleep(7)
browser.quit()
