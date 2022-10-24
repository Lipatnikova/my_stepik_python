# 3_4_2_test_fixture1.py

from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

'''
Для себя сделал шпаргалку, что бы все в одном месте по маркировке и пропускам(постарался вместить основное на мой взгляд)
После маркировок @pytest.mark..., через двоеточие указывал команду для запуска скрипта
Может кому тоже пригодится..

Маркировка тестов и пропуск тестов

# Запустится только smoke:
@pytest.mark.smoke : pytest -s -v -m smoke test_fixture.py

# Запуска всех тестов, не отмеченных как smoke:
@pytest.mark.smoke : pytest -s -v -m "not smoke" test_fixture.py

# Запуск тестов с разными маркировками:
@pytest.mark.smoke
@pytest.mark.regression : pytest -s -v -m "smoke or regression" test_fixture.py

# Запуск тестов имеющих несколько маркировок:
@pytest.mark.smoke
@pytest.mark.win10 : pytest -s -v -m "smoke and win10" test_fixture.py

# Пропуск тестов:
@pytest.mark.skip : pytest -s -v  test_fixture.py

# Помечать тест как ожидаемо падающий(пометка:XFAIL):
# упавший тест теперь отмечен как xfail, но результат прогона тестов помечен как успешный
# Когда баг починят, мы это узнаем, так как тест будет отмечен как XPASS
@pytest.mark.xfail : pytest -rx -v test_fixture.py

# reason - Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rX
@pytest.mark.xfail(reason="fixing this bug right now") : pytest -rX -v test_fixture.py

# Параметр strict
# Ни XFAIL, ни XPASS по умолчанию не приводят к падению всего набора тестов.
# Но это можно изменить, установив параметру strict значение True:
# В этом случае, если тест будет неожиданно пройден (XPASS),
# то это приведет к падению всего тестового набора
@pytest.mark.xfail(strict=True) : pytest -rX -v test_fixture.py
'''