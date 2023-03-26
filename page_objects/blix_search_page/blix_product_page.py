from page_objects.abstract.abs_base_page import AbsBasePage
from web_elements.image import Image
from web_elements.link import Link
from web_elements.text import Text
from .blix_product_page_locators import BlixProductPageLocators as Loc


class BlixProductPage(AbsBasePage):

    product_name = Text(Loc.PRODUCT_NAME)
    store_name = Text(Loc.STORE_NAME)
    price = Text(Loc.PRICE)
    leaflet_img = Image(Loc.LEAFLET_IMG)
    leaflet_link = Link(Loc.LEAFLET_LINK)

    def wait_for_page_to_load(self, timeout: int = 30):
        self.wait_for_visibility_of_element_located(locator=Loc.PRODUCT_NAME,
                                                    timeout=timeout)

    def is_page_displayed(self):
        return self.is_element_located_displayed(Loc.PRODUCT_NAME)

    def get_leaflet_origin_url(self):
        element = self.driver.find_element(*Loc.PRODUCT_NAME)
        return element.get_attribute("href")
