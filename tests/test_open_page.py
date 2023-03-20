from hamcrest import assert_that
from pytest import fixture

from page_objects.blix_search_page.blix_product_page import BlixProductPage
from page_objects.blix_search_page.blix_search_page import BlixSearchPage
from page_objects.blix_search_page.consent_container_page_object import ConsentContainerPageObject

from conf.urls import *

phrase = "napój-owsiany"
url = SEARCH_PAGE.format(phrase)


@fixture
def search_page(driver):
    page = BlixSearchPage(driver, url)
    page.open()
    page.wait_for_page_to_load()

    consent_container = ConsentContainerPageObject(driver)
    consent_container.wait_for_object_to_load()
    consent_container.do_not_consent.click()

    return page


def test_open_search_page(driver, search_page):

    assert_that(search_page.is_page_displayed(), "Page not displayed properly")

    assert_that(len(search_page.leaflet_list) > 0, "Could not detect any leaflets")
    assert_that(len(search_page.product_list) > 0, "Could not detect any products")

    assert_that(search_page.leaflet_count == len(search_page.leaflet_list), "Mismatch while detecting leaflet count")
    assert_that(search_page.product_count == len(search_page.product_list), "Mismatch while detecting product count")


def test_open_product_page(driver, search_page):

    product = search_page.product_list[0]
    search_page.scroll_into_view(product.name)
    product.name.click()

    product_page = BlixProductPage(driver)
    product_page.wait_for_page_to_load()

    assert_that(product_page.is_page_displayed(), "Product page is not displayed")


# def test_expandable_lists(driver):
#     pass


# def test_nonexpandable_lists(driver):
#     pass

