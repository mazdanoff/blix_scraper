from selenium.webdriver.remote.webelement import WebElement

from page_objects.abstract.abs_base_page import AbsBasePage
from web_elements.button import Button
from web_elements.text import Text
from .blix_search_leaflet_list import LeafletList
from .blix_search_product_list import ProductList
from .blix_search_page_locators import BlixSearchPageLocators as Loc


class BlixSearchPage(AbsBasePage):

    _leaflet_count = Text(Loc.LEAFLET_COUNT)
    leaflet_list = LeafletList(*Loc.LEAFLETS_SECTION)
    leaflet_expand_button = Button(Loc.LEAFLET_EXPAND_BUTTON)

    _product_count = Text(Loc.PRODUCT_COUNT)
    product_list = ProductList(*Loc.PRODUCTS_SECTION)
    product_expand_button = Button(Loc.PRODUCT_EXPAND_BUTTON)

    @property
    def leaflet_count(self):
        return int(self._leaflet_count.value)

    @property
    def product_count(self):
        return int(self._product_count.value)

    def wait_for_page_to_load(self, timeout: int = 30):
        self.wait_for_visibility_of_element_located(
            locator=self.leaflet_list.get_headers_locator(),
            timeout=timeout)

    def is_page_displayed(self):
        return self.is_element_located_displayed(self.leaflet_list.get_headers_locator())

    def expand_leaflet_list(self):
        button = self.leaflet_expand_button.element
        if self._is_button_enabled(button):
            self.scroll_into_view(button)
            button.click()
        self.scroll_into_view(self.leaflet_list[len(self.leaflet_list)-1].store)

    def expand_product_list(self):
        button = self.product_expand_button.element
        if self._is_button_enabled(button):
            self.scroll_into_view(button)
            button.click()

    @staticmethod
    def _is_button_enabled(button: WebElement):
        # enabled button has no 'disabled' attribute
        return button.get_attribute("disabled") is None
