from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_basket_button()

        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

        self.solve_quiz_and_get_code()

        self.check_basket_price()

        self.message_succesful_added_product()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Add-to-basket button  is not presented"

    def message_succesful_added_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == message_product_name, "Names don't match"

    def check_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price in basket_price, "The numbers don't match"