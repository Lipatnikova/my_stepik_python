# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        # Если
        # нужно
        # проверить, что
        # тест
        # вызывает
        # ожидаемое
        # исключение
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()
