from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage): 

    def should_be_empty_basket(self):
    	assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Some product in bakset, but should not be"


    def should_be_empty_basket_text(self):
    	assert self.is_element_present(*BasketPageLocators.EMPTY_BAKSET_TEXT), "Empty basket text is not present, but should be"


