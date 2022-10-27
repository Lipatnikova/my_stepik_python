'''
сценарием действий:
1 открыть страницу
2 ввести правильный ответ
3 нажать кнопку "Отправить"
4 дождаться фидбека о том, что ответ правильный
5 проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

настройте нужные ожидания, чтобы тесты работали стабильно.

В упавших тестах найдите кусочки послания. Тест должен падать, если текст
в опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки
текста в одно предложение и отправьте в качестве ответа на это задание.
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import math
import time


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestAnswerForTextArea:


    @pytest.mark.parametrize('num', ["236895", "236896", "236897", "236898",
                                     "236899", "236903", "236904", "236905"])
    def test_find_textarea_send_answer(self, browser, num):
        link = f"https://stepik.org/lesson/{num}/step/1"
        browser.get(link)

        # textarea = WebDriverWait(browser, 10).until(
        #     EC.presence_of_element_located(By.XPATH, "//textarea[1]"))

        textarea = browser.find_element(By.XPATH, "//textarea[1]")
        answer = math.log(int(time.time()))
        textarea.send_keys(answer)
        # btn = WebDriverWait(browser, 10).until(
        #     EC.element_to_be_clickable(By.CLASS_NAME, 'submit-submission'))
        btn = browser.find_element(By.CLASS_NAME, 'submit-submission')
        btn.click()

        # WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.CLASS_NAME, 'smart-hints__hint'))
        message = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
        assert 'Correct' in message.text


if __name__ == '__main__':
    pytest.main()
