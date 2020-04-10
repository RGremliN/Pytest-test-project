from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
        
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_TITLE_ON_PAGE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_TITLE_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")

    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    BASKET_PRICE_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID  = (By.CSS_SELECTOR, "#login_link_inc")
    HEADER_BASKET_BUTTON_LINK = (By.CSS_SELECTOR, ".header .basket-mini .btn-group a.btn.btn-default")

class BasketPageLocators():
    EMPTY_BAKSET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
