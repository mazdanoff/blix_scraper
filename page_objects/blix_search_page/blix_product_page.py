from page_objects.abstract.abs_base_page import AbsBasePage
from .blix_product_page_locators import BlixProductPageLocators as Loc


class BlixProductPage(AbsBasePage):

    def wait_for_page_to_load(self, timeout: int = 30):
        self.wait_for_visibility_of_element_located(locator=Loc.PRODUCT_NAME,
                                                    timeout=timeout)

    def is_page_displayed(self):
        self.is_element_located_displayed(Loc.PRODUCT_NAME)
