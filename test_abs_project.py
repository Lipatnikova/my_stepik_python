from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest
import time


def sel(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first").send_keys('Tom')
    browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second").send_keys('Moju')
    browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third").send_keys("wer@gmail.com")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    return welcome_text


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            sel(link),
            "Congratulations!"
        )

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            sel(link),
            "Congratulations!"
        )

if __name__ == '__main__':
    unittest.main()

