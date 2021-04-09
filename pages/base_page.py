from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    URL = "https://duckduckgo.com/"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator, time=5) -> WebElement:
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=5) -> list[WebElement]:
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def get_title(self):
        return self.driver.title
