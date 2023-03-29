from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.blix_search_page.blix_product_page import BlixProductPage
from scripts import scrape_data as blix
from scripts.saledata import ProductData, SaleData


def get_sales(driver: WebDriver, phrase):

    products = list()
    page = blix.setup_search_page(driver, phrase)
    leaflets, product_urls = blix.prepare_search_data(page)
    leaflets = {leaflet.leaflet_link: leaflet for leaflet in leaflets}

    for url in product_urls:
        page = BlixProductPage(driver).open(url)
        page.wait_for_page_to_load()
        product = ProductData(name=page.product_name.text,
                              price=page.price.text,
                              store=page.store_name.text,
                              link_to_img=page.leaflet_img.src,
                              leaflet_link=page.leaflet_link.link)
        products.append(product)
        if product.leaflet_link in leaflets:
            sale = SaleData(name=product.name,
                            price=product.price,
                            store=product.store,
                            time=leaflets[product.leaflet_link].time,
                            link_to_img=product.link_to_img,
                            leaflet_link=product.leaflet_link)
            yield sale