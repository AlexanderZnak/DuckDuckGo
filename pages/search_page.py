import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    _SEARCH_INPUT = (By.ID, "search_form_input_homepage")
    _SEARCH_BUTTON = (By.ID, "search_button_homepage")
    _LIST_OF_RESULTS_PERTAIN_SEARCH_TEXT = (By.CSS_SELECTOR, ".acp")

    def open_page(self):
        self.driver.get(self.URL)
        return self

    def fill_in_search_field(self, phrase):
        self.find_element(self._SEARCH_INPUT).send_keys(phrase)
        self.driver.get_screenshot_as_png()
        return self

    def click_search_button(self):
        self.find_element(self._SEARCH_BUTTON).click()
        return self

    def get_all_values_of_suggestions_pertain_search_text(self):
        list_of_suggestions = self.get_all_suggestions()
        value_of_suggestions = [suggestion.text for suggestion in list_of_suggestions]
        return value_of_suggestions

    def get_random_suggestion(self):
        return self.get_all_suggestions()[random.randint(0, len(self.get_all_suggestions()) - 1)]

    def get_all_suggestions(self):
        return self.find_elements(self._LIST_OF_RESULTS_PERTAIN_SEARCH_TEXT)

    def click_by_auto_complete_suggestion(self, suggestion):
        suggestion.click()
        return self
