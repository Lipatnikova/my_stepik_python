'''
 добавили фикстуру browser, которая создает нам экземпляр браузера
 для тестов в данном файле. Когда файлов с тестами становится больше
 одного, приходится в каждом файле с тестами описывать данную фикстуру.
 Это очень неудобно. Для хранения часто употребимых фикстур и хранения
 глобальных настроек нужно использовать файл conftest.py, который должен
 лежать в директории верхнего уровня в вашем проекте с тестами. Можно
 создавать дополнительные файлы conftest.py в других директориях, но
 тогда настройки в этих  файлах будут применяться только к тестам
 в под-директориях.
'''

# 3_6_2

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

# 3_6_6
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    # options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
    # browser = webdriver.Chrome(options=options)

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
