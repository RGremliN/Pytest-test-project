from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_success_message_contains_product_title(self):
        product_title_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_ON_PAGE).text
        product_title_in_success_message = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_IN_SUCCESS_MESSAGE).text

        assert product_title_in_success_message == product_title_on_page, f"{product_title_in_success_message} is not equal{product_title_on_page}"

    def should_be_basket_price_in_success_message_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price_in_success_messgae = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_SUCCESS_MESSAGE).text

        assert basket_price_in_success_messgae == product_price, f"{basket_price_in_success_messgae} is not equal {product_price}"



