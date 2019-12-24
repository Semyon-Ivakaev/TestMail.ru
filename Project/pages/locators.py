from selenium.webdriver.common.by import By

class BasePageLocators():
    INPUT_SQUAD = (By.CSS_SELECTOR, "input#q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[value='Найти']")
    SEARCH_RESULT = (By.CSS_SELECTOR, "div.top_menu__wrapper")
    TOP_NEWS = (By.CSS_SELECTOR, ".news.news_x-xs h3")
    OTHER_NEWS = (By.CSS_SELECTOR, ".news.news_x-xs a:nth-child(2)")
    REGION_NEWS = (By.CSS_SELECTOR, ".tabs.tabs_x-xs a:nth-child(2)")
    REGION_TOP_NEWS = (By.CSS_SELECTOR, ".mediaprojects h3")
    INPUT_EMAIL = (By.CSS_SELECTOR, "div input.input")
    BUTTON_INPUT_PASSWORD = (By.CSS_SELECTOR, "input.o-control")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    BUTTON_INPUT = (By.CSS_SELECTOR, "input[type='submit']")
    BUTTON_EXIT = (By.CSS_SELECTOR, "#PH_logoutLink")
