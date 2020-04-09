from selenium.common.exceptions import NoSuchElementException

class BasePage():
    #конструктор — метод, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    #открыть нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    #вспомогательный метод поиска элемента в нашей базовой странице BasePage, который будет возвращать нам True или False
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True









