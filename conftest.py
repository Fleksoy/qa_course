import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)


# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
def pytest_addoption(parser):
    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help='Language')


# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def browser(request):
    browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart Сhrome browser for test..")
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs',{'intl.accept_languages' : language})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart Firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    time.sleep(3)
    browser.quit()