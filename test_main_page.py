import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        yield

    def test_guest_should_see_login_link(self,browser):
        self.page.go_to_login_page()        # выполняем метод страницы - переходим на страницу логина
        self.page.should_be_login_link()    # проверяем что есть ссылка на страницу логина


    def test_guest_can_go_to_login_page(self,browser):
        self.page.go_to_login_page()        # выполняем метод страницы - переходим на страницу логина
        self.page = LoginPage(browser, self.link)# инициализируем объект для страницы логина
        self.page.should_be_login_page()    # проверяем что мы перешли на страницу логина


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу
    page.go_to_basket_page_by_header_button()
    page = BasketPage(browser, link)
    page.should_be_empty_basket()
    page.should_be_empty_basket_text()









