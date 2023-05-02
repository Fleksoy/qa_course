from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.skip
@pytest.mark.login_page
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.product_page
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, f"{link}")
    page.open()
    page.add_product_to_basket()
    page.check_basket_price()
    page.message_succesful_added_product()


@pytest.mark.skip
@pytest.mark.product_page
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.message_is_not_present()


@pytest.mark.skip
@pytest.mark.product_page
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser,link)
    page.open()
    page.message_is_not_present()


@pytest.mark.skip
@pytest.mark.product_page
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.message_is_disappeared()


@pytest.mark.skip
@pytest.mark.product_page
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
@pytest.mark.product_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
@pytest.mark.main_page
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket()
    page.dont_have_products_in_basket()
    page.empty_basket_message()



@pytest.mark.product_page
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket()
    page.dont_have_products_in_basket()
    page.empty_basket_message()

# pytest -v -m main_page  --tb=line  test_main_page.py