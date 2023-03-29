from typing import List

from selenium.webdriver.remote.webelement import WebElement

from page_objects.abstract.abs_base_page import AbsBasePage
from scripts.saledata import LeafletData
from utils.wait_until import wait_until
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
        return int(self._leaflet_count.text)

    @property
    def product_count(self):
        return int(self._product_count.text)

    def wait_for_page_to_load(self, timeout: int = 30):
        self.wait_for_visibility_of_element_located(
            locator=self.leaflet_list.get_headers_locator(),
            timeout=timeout)

    def is_page_displayed(self):
        return self.is_element_located_displayed(self.leaflet_list.get_headers_locator())

    def is_leaflet_list_displayed(self):
        return self.is_element_located_displayed(self.leaflet_list.get_headers_locator())

    def is_product_list_displayed(self):
        return self.is_element_located_displayed(self.product_list.get_headers_locator())

    def expand_leaflet_list(self):
        button = self.leaflet_expand_button.element
        if self._is_button_enabled(button):
            self.scroll_into_view(button)
            button.click()
            wait_until(self._are_expanded_leaflets_readable)
        self.scroll_into_view(self.leaflet_list[len(self.leaflet_list)-1].store)

    def expand_product_list(self):
        button = self.product_expand_button.element
        if self._is_button_enabled(button):
            self.scroll_into_view(button)
            button.click()

    def get_leaflet_list(self) -> List[LeafletData]:
        leaflet_list = list()
        for leaf in self.leaflet_list:
            leaflet = LeafletData(store=leaf.store.text,
                                  time=leaf.time.text,
                                  leaflet_link=leaf.leaflet_page.get_attribute('href'))
            leaflet_list.append(leaflet)
        return leaflet_list

    def get_product_page_urls(self) -> List[str]:
        urls = list()
        for product in self.product_list:
            href = product.name.get_attribute('href')
            urls.append(href)
        return urls

    @staticmethod
    def _is_button_enabled(button: WebElement):
        # enabled button has no 'disabled' attribute
        return button.get_attribute("disabled") is None

    def _are_expanded_leaflets_readable(self):
        # collapsed list hides bottom items as shadow elements
        # shadowed elements' text is an empty string
        # this method should be called if list was expanded first
        return self.leaflet_list[len(self.leaflet_list)-1].store.text != ""
