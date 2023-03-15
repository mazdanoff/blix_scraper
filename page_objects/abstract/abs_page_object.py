from time import sleep
from typing import Tuple

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AbsPageObject:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_element_located_present(self, locator: Tuple[str, str]):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_located_displayed(self, locator: Tuple[str, str]) -> bool:
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def wait_for_presence_of_element_located(self, locator, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            pass

    def wait_for_visibility_of_element_located(self, locator, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
        except TimeoutException:
            pass

    @staticmethod
    def wait(seconds):
        sleep(seconds)

    def scroll_into_view(self, element: WebElement):
        self.driver.execute_script(f"arguments[0].scrollIntoView(false)", element)
        self.wait(0.5)
        # no fear
        # <obscuring elements with fixed position lurking at viewport's bottom>
        # one fear
        self.driver.execute_script(f"window.scrollBy(0, {element.size['height']})")
        self.wait(0.5)
