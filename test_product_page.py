import pytest

from pages.product_page import ProductPage

@pytest.mark.parametrize('promo_offer', ['newYear','newYear2019','offer0','offer1','offer2','offer3','offer4','offer5','offer6',pytest.param("offer7", marks=pytest.mark.xfail),'offer8','offer9'])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=" + promo_offer
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_contains_product_title()
    page.should_be_basket_price_in_success_message_equal_product_price()




