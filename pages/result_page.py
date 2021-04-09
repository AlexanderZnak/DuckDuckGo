import random
import time

from selenium.webdriver.common.by import By

from elements.dropdown import DropDown
from pages.base_page import BasePage


class ResultPage(BasePage):
    _LIST_OF_ALL_RESULTS = (By.CSS_SELECTOR, ".result__a")
    _MORE_RESULTS_BUTTON = (By.ID, "rld-1")
    _SEARCH_FIELD_INPUT = (By.ID, "search_form_input")
    _SEARCH_BUTTON = (By.ID, "search_button")
    _DUCK_BAR_REFERENCES = "//*[@id='duckbar_static']//*[contains(text(),'{}')]"
    _ALL_IMAGES = (By.CSS_SELECTOR, ".tile--img__img")
    _REGION_SWITCHER = (By.CSS_SELECTOR, ".switch")
    _SETTINGS_SWITCHERS = "//*[contains(text(), '{}')]/parent::div//*[contains(@class,'frm__switch__label')]"

    def get_all_links_values(self):
        lists_of_search_results = self.get_all_links()
        values_of_search_results = [link.text for link in lists_of_search_results]
        return values_of_search_results

    def click_more_results_button(self):
        self.find_element(self._MORE_RESULTS_BUTTON).click()
        return self

    def click_by_result_link(self, link):
        link.click()
        return self

    def get_all_links(self):
        return self.find_elements(self._LIST_OF_ALL_RESULTS)

    def get_random_link(self):
        return self.get_all_links()[random.randint(0, len(self.get_all_links()) - 1)]

    def get_search_value(self):
        return self.find_element(self._SEARCH_FIELD_INPUT).get_attribute("value")

    def clear_search_input(self):
        self.find_element(self._SEARCH_FIELD_INPUT).clear()
        return self

    def fill_in_search_field_new_search_text(self, phrase):
        self.find_element(self._SEARCH_FIELD_INPUT).send_keys(phrase)
        return self

    def click_search_button(self):
        self.find_element(self._SEARCH_BUTTON).click()
        return self

    def click_to_switch_results_items_by(self, reference):
        locator = (By.XPATH, self._DUCK_BAR_REFERENCES.format(reference))
        self.find_element(locator).click()
        return self

    def get_all_img_attr(self):
        list_of_images_elements = self.get_all_images_elements()
        list_of_img_attr = [value.tag_name for value in list_of_images_elements]
        return list_of_img_attr

    def get_all_images_elements(self):
        return self.find_elements(self._ALL_IMAGES)

    def is_item_bar_active(self, reference):
        locator = (By.XPATH, self._DUCK_BAR_REFERENCES.format(reference))
        class_value: str = self.find_element(locator).get_attribute("class")
        is_item_active = False
        for is_active in class_value.split():
            if is_active == "is-active":
                is_item_active = True
        return is_item_active

    def click_by_all_regions(self):
        DropDown("All Regions", self.driver) \
            .click_by_filter()
        return self

    def select_particular_region(self, region_name):
        DropDown("All Regions", self.driver) \
            .select_particular_item(region_name)
        return self

    def is_region_selected(self, region_name):
        return DropDown(region_name, self.driver) \
            .is_item_selected()

    def is_switcher_enabled(self):
        is_enabled = False
        classes_in_switcher_element: str = self.find_element(self._REGION_SWITCHER).get_attribute("class")
        for class_is_on in classes_in_switcher_element.split():
            if class_is_on == "is-on":
                is_enabled = True
        return is_enabled

    def click_by_settings(self):
        DropDown("Settings", self.driver).click_by_filter()
        return self

    def click_by_switcher(self, new_tab_switcher):
        locator = (By.XPATH, self._SETTINGS_SWITCHERS.format(new_tab_switcher))
        self.find_element(locator).click()

        # Be required to refresh the page due to settings does not work without it
        self.driver.refresh()
        return self

    def do_scrolling_down(self):
        scroll_pause_time = 0.5

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        return self
