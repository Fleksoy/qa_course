from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)  #  Конструктор с ключевым словом super вызывает конструктор класса предка и передает ему аргументы, которые передали в конструктор MainPage

