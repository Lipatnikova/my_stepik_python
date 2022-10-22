# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/get_attribute.html"
# browser = webdriver.Chrome()
# browser.get(link)
# time.sleep(2)
# # замена заголовка страницы + изм текст в alert (всплывающее окно)
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element(By.ID, 'input_value').text
y = calc(x)
browser.find_element(By.ID, 'answer').send_keys(y)


robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
browser.find_element(By.ID, 'robotCheckbox').click()

robotsRule = browser.find_element(By.ID, 'robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
browser.find_element(By.ID, 'robotsRule').click()

button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(5)
browser.quit()

'''
Как вариант еще можно скрывать ненужный элемент

browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
Еще в глобальном смысле мотнуть в самый верх или самый низ страницы можно и питоном для тега body

from selenium.webdriver.common.keys import Keys

browser.find_element_by_tag_name('body').send_keys(Keys.END) #или Home если наверх
'''

