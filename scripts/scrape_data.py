from typing import List, Tuple

from selenium.webdriver.remote.webdriver import WebDriver

from conf.urls import SEARCH_PAGE
from page_objects.blix_search_page.blix_product_page import BlixProductPage
from page_objects.blix_search_page.blix_search_page import BlixSearchPage
from page_objects.blix_search_page.consent_container_page_object import ConsentContainerPageObject
from scripts.driver import Driver
from scripts.saledata import SaleData, LeafletData, ProductData


def setup_search_page(driver, phrase):

    # Open the search page directly at results.
    url = SEARCH_PAGE.format(phrase)
    page = BlixSearchPage(driver, url)
    page.open().wait_for_page_to_load()

    # consent box pops up every time and I have no mana to handle cookies
    consent_container = ConsentContainerPageObject(driver)
    consent_container.wait_for_object_to_load()
    consent_container.do_not_consent.click()

    return page


def prepare_search_data(page):

    leaflet_list = list()
    # 1. Gather data from all leaflets. Product names and prices are not mentioned here.
    if page.is_leaflet_list_displayed():
        page.expand_leaflet_list()
        leaflet_list.extend(page.get_leaflet_list())
        page.wait(1)

    # 2. Collect urls of each listed product
    urls = list()
    if page.is_product_list_displayed():
        page.expand_product_list()
        urls.extend(page.get_product_page_urls())

    return leaflet_list, urls


def get_all_sale_data(driver: WebDriver, phrase: List[str]) -> Tuple[List[LeafletData],
                                                                 List[ProductData],
                                                                 List[SaleData]]:
    products = list()
    sales = list()
    page = setup_search_page(driver, phrase)
    leaflets, product_urls = prepare_search_data(page)

    # 3. Open gathered urls one by one
    for url in product_urls:
        # 3a) Scrape data from a page
        page = BlixProductPage(driver).open(url)
        page.wait_for_page_to_load()
        product = ProductData(name=page.product_name.text,
                              price=page.price.text,
                              store=page.store_name.text,
                              link_to_img=page.leaflet_img.src,
                              leaflet_link=page.leaflet_link.link)
        products.append(product)

    # 3. Pair up products with leaflets to retrieve full sale data.
    # 3a) LeafletData and ProductData share leaflet_link field. Pairing is based on this field's value.
    #     If a match is found, it means product is included in the leaflet and forms a full sale data set.

    for leaflet in leaflets:
        for product in products:
            if leaflet.leaflet_link == product.leaflet_link:
                sale = SaleData(name=product.name,
                                price=product.price,
                                store=product.store,
                                time=leaflet.time,
                                link_to_img=product.link_to_img,
                                leaflet_link=product.leaflet_link)
                sales.append(sale)

    return leaflets, products, sales


def find_sales(phrase):
    with Driver() as driver:
        return get_all_sale_data(driver, phrase)


if __name__ == '__main__':
    phrase = "napój owsiany"
    phrase = phrase.split(" ")
    leaf, prod, sale = find_sales(phrase)
    for leaflet in leaf:
        print(leaflet)
    for product in prod:
        print(product)
    for sale in sale:
        print(sale)
