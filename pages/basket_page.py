from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def dont_have_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Item is present"

    def empty_basket_message(self):
        assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.BASKET_INNER).text, 'No text about empty basket'