import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# @pytest.fixture(scope='function')
def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print('\nquit browser...')
    browser.quit()

#
# from webdriver_manager.chrome import DriverManager
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math

# driver = webdriver.Chrome(DriverManager().install())

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# browser = webdriver.Chrome(DriverManager().install())
url = 'http://suninjuly.github.io/alert_accept.html'
browser.get(url)

browser.find_element(By.TAG_NAME, 'button').click()

alert = browser.switch_to.alert
alert.accept()

x = calc(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.ID, 'answer').send_keys(x)


browser.find_element(By.TAG_NAME, 'button').click()
