# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as browser:
#     result = []
#     browser.get('http://parsinger.ru/blank/2/1.html')
#     time.sleep(1)
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
#     browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
#
#     time.sleep(1)
#     for x in reversed(range(len(browser.window_handles))):
#         browser.switch_to.window(browser.window_handles[x])
#         for y in browser.find_elements(By.CLASS_NAME, 'check'):
#             y.click()


from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(url)
browser.find_element(By.TAG_NAME, 'button').click()

# переход на новую вкладку, если их 2
browser.switch_to.window(browser.window_handles[1])

input_value = browser.find_element(By.ID, 'input_value')
x = browser.find_element(By.ID, 'input_value').text
x = calc(x)
browser.find_element(By.ID, 'answer').send_keys(x)
browser.find_element(By.TAG_NAME, 'button').click()

# код из всплывающего окна
alert = browser.switch_to.alert
alert_text = alert.text
password = (browser.switch_to.alert.text).split(" ")[-1]

print(password)
browser.quit()
