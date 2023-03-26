from typing import List, Tuple

from conf.urls import SEARCH_PAGE
from page_objects.blix_search_page.blix_product_page import BlixProductPage
from page_objects.blix_search_page.blix_search_page import BlixSearchPage
from page_objects.blix_search_page.consent_container_page_object import ConsentContainerPageObject
from scripts.driver import Driver
from scripts.saledata import SaleData, LeafletData, ProductData

# phrase = "napój-owsiany"
phrase = "ser-mozzarella"
url = SEARCH_PAGE.format(phrase)


def print_leaflet_data(leaflet_list: List[LeafletData]):
    for leaflet in leaflet_list:
        print(leaflet)


def print_product_data(product_list: List[ProductData]):
    for product in product_list:
        print(product)


def print_sale_data(sale_list: List[SaleData]):
    for sale in sale_list:
        print(sale)


def get_data():
    with Driver() as driver:
        return get_sale_data(driver)


def get_sale_data(driver) -> Tuple[List[LeafletData],
                                   List[ProductData],
                                   List[SaleData]]:
    """
    :param driver: WebDriver element, preferably within a context manager
    """
    sale_data_list = list()
    leaflet_list = list()
    product_list = list()

    # 0. Setup. Open the page.
    page = BlixSearchPage(driver, url)
    page.open()
    page.wait_for_page_to_load()

    # 0a) consent box pops up every time and I have no mana to handle cookies
    consent_container = ConsentContainerPageObject(driver)
    consent_container.wait_for_object_to_load()
    consent_container.do_not_consent.click()

    # 0b) In case each list has more than 8 entries, lists will need to be expanded first.
    # Otherwise, data cannot be read, as non-expanded elements are shadowed.
    page.expand_product_list()
    page.expand_leaflet_list()

    # 1. Gather data from all leaflets. Product names and prices are not mentioned here.
    for leaf in page.leaflet_list:
        leaflet = LeafletData(store=leaf.store.text,
                              time=leaf.time.text,
                              leaflet_link=leaf.leaflet_page.get_attribute('href'))
        leaflet_list.append(leaflet)

    # 2. Gather data from all products

    # 2a) Collect urls of each listed product
    product_urls = list()

    for product in page.product_list:
        href = product.name.get_attribute('href')
        product_urls.append(href)

    # 2b) Open gathered urls one by one and scrape data from each page
    for url_ in product_urls:
        page = BlixProductPage(driver).open(url_)
        page.wait_for_page_to_load()
        product = ProductData(name=page.product_name.text,
                              price=page.price.text,
                              store=page.store_name.text,
                              link_to_img=page.leaflet_img.src,
                              leaflet_link=page.leaflet_link.link)
        product_list.append(product)

    # 3. Pair up products with leaflets to retrieve full sale data.

    # 3a) LeafletData and ProductData share leaflet_link field. Pairing is based on this field's value.
    # If a match is found, it means product is included in the leaflet and forms a full sale data set.

    for leaflet in leaflet_list:
        for product in product_list:
            if leaflet.leaflet_link == product.leaflet_link:
                sale = SaleData(name=product.name,
                                price=product.price,
                                store=product.store,
                                time=leaflet.time,
                                link_to_img=product.link_to_img,
                                leaflet_link=product.leaflet_link)
                sale_data_list.append(sale)

    return leaflet_list, product_list, sale_data_list


if __name__ == '__main__':
    leaf, prod, sale = get_data()
    print_leaflet_data(leaf)
    print_product_data(prod)
    print_sale_data(sale)
