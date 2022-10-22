from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/alert_accept.html'
browser.get(url)

browser.find_element(By.TAG_NAME, 'button').click()

alert = browser.switch_to.alert
alert.accept()

x = calc(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.ID, 'answer').send_keys(x)


browser.find_element(By.TAG_NAME, 'button').click()
