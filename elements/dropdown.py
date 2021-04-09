from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DropDown(BasePage):
    _FILTER = "//*[contains(@class,'dropdown__button') and contains(text(), '{}')]"
    _ITEM = "//*[contains(@class,'modal__list') and contains(text(), '{}')]"

    def __init__(self, filter_name, driver: WebDriver):
        super().__init__(driver)
        self.filter_name = filter_name

    def click_by_filter(self):
        locator = (By.XPATH, self._FILTER.format(self.filter_name))
        self.find_element(locator).click()
        return self

    def select_particular_item(self, item_name):
        locator = (By.XPATH, self._ITEM.format(item_name))
        self.find_element(locator).click()
        return self

    def is_item_selected(self):
        locator = (By.XPATH, self._FILTER.format(self.filter_name))
        is_selected = True
        try:
            self.find_element(locator)
        except TimeoutException:
            is_selected = False
        return is_selected
