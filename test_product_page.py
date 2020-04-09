import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage

@pytest.mark.skip
@pytest.mark.parametrize('promo_offer', ['newYear','newYear2019','offer0','offer1','offer2','offer3','offer4','offer5','offer6',pytest.param("offer7", marks=pytest.mark.xfail),'offer8','offer9'])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=" + promo_offer
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_contains_product_title()
    page.should_be_basket_price_in_success_message_equal_product_price()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу
    page.go_to_login_page() 
    page = LoginPage(browser, link)       # выполняем метод страницы - переходим на страницу логина
    page.should_be_login_page()    # проверяем что мы перешли на страницу логина   

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу 
    page.add_product_to_basket() 
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser ):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу 
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу
    page.add_product_to_basket()
    page.should_be_success_message_is_disappeared()

