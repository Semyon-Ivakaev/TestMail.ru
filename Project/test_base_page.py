import time
import pytest
from .pages.main_page import MainPage
from .pages.base_page import BasePage

class TestGuest:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        pass

    def test_guest_autorisation(self, browser):
        link = 'https://mail.ru/'
        page = MainPage(browser, link)
        page.open()
        email = 'blabla@mail.ru'
        password = 'oooyMy'
        time.sleep(1)
        page.guest_autorisation(email, password)

    def test_guest_search_date(self, browser):
        link = 'https://mail.ru/'
        info = 'Python + Selenium = <3'
        page = MainPage(browser, link)
        page.open()
        page.guest_search_date(info)
        time.sleep(1)

    def test_guest_read_news(self, browser):
        link = 'https://mail.ru/'
        page = MainPage(browser, link)
        page.open()
        page.guest_read_top_news()
        page.guest_read_region_news()


