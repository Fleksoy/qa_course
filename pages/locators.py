from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRER_FORM_PASSWORD_CONFIRMED = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRER_FORM_SUBMIT = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BASKET_PRICE = (By.CSS_SELECTOR, '.basket-mini.pull-right ')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alertinner strong')
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, '#messages .alertinner')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, "#basket_formset .basket-items .row")
    BASKET_INNER = (By.CSS_SELECTOR, "#content_inner")