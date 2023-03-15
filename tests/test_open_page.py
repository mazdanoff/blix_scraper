from hamcrest import assert_that

from page_objects.blix_search_page.blix_search_page import BlixSearchPage
from page_objects.blix_search_page.consent_container_page_object import ConsentContainerPageObject

from conf.urls import *

phrase = "napój-owsiany"
url = SEARCH_PAGE.format(phrase)


def test_open_blix(driver):

    page = BlixSearchPage(driver, url)
    page.open()
    page.wait_for_page_to_load()

    consent_container = ConsentContainerPageObject(driver)
    consent_container.wait_for_object_to_load()
    consent_container.do_not_consent.click()

    assert_that(page.is_page_displayed(), "Page not displayed properly")
    assert_that(page.leaflet_count == len(page.leaflet_list), "Mismatch while detecting leaflet count")


def test_expandable_lists(driver):
    pass


def test_nonexpandable_lists(driver):
    pass

