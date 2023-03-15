from page_objects.abstract.abs_page_object import AbsPageObject
from web_elements.button import Button
from .consent_container_page_object_locators import ConsentContainerPageObjectLocators as Loc


class ConsentContainerPageObject(AbsPageObject):

    do_not_consent = Button(Loc.DO_NOT_CONSENT)

    def wait_for_object_to_load(self, timeout=30):
        self.wait_for_visibility_of_element_located(Loc.DO_NOT_CONSENT,
                                                    timeout=timeout)
