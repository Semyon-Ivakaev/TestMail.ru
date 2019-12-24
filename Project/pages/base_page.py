import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def guest_search_date(self, info):
        input_squad = self.browser.find_element(*BasePageLocators.INPUT_SQUAD).send_keys(info)
        search_button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON).click()
        search_result = self.browser.find_element(*BasePageLocators.SEARCH_RESULT)
        assert search_result, "Search failed"


    def guest_read_top_news(self):
        first_window = self.browser.window_handles[0]
        click_top_news = self.browser.find_element(*BasePageLocators.TOP_NEWS).click()
        new_window = self.browser.window_handles[1]
        assert new_window, "New window dont open"

        self.browser.switch_to.window(new_window)
        self.browser.close()
        self.browser.switch_to.window(first_window)

        time.sleep(1)
        click_other_news = self.browser.find_element(*BasePageLocators.OTHER_NEWS).click()
        second_window = self.browser.window_handles[1]
        assert second_window, "Second winwod dont open"
        time.sleep(1)

        self.browser.switch_to.window(second_window)
        self.browser.close()
        self.browser.switch_to.window(first_window)

    def guest_read_region_news(self):
        self.browser.find_element(*BasePageLocators.REGION_NEWS).click()
        self.browser.find_element(*BasePageLocators.REGION_TOP_NEWS).click()

    def guest_autorisation(self, email, password):
        self.browser.find_element(*BasePageLocators.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*BasePageLocators.BUTTON_INPUT_PASSWORD).click()
        time.sleep(1)
        self.browser.find_element(*BasePageLocators.INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*BasePageLocators.BUTTON_INPUT).click()
        button_exit = self.browser.find_element(*BasePageLocators.BUTTON_EXIT)
        assert button_exit, "You not autorisation"
        time.sleep(3)