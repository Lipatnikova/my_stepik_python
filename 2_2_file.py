import os
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element(By.NAME, 'firstname').send_keys('Bob')
browser.find_element(By.NAME, 'lastname').send_keys('Black')
browser.find_element(By.NAME, 'email').send_keys('bob@gmail.com')

current_dir = os.path.abspath(os.path.dirname(__file__))
# получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')
# добавляем к этому пути имя файла
browser.find_element(By.ID, 'file').send_keys(file_path)

browser.find_element(By.TAG_NAME, 'button').click()


