from conf.urls import SEARCH_PAGE
from page_objects.blix_search_page.blix_product_page import BlixProductPage
from page_objects.blix_search_page.blix_search_page import BlixSearchPage
from page_objects.blix_search_page.consent_container_page_object import ConsentContainerPageObject
from scripts.driver import Driver

# phrase = "napój-owsiany"
phrase = "ser-mozzarella"
url = SEARCH_PAGE.format(phrase)


def get_data():
    with Driver() as driver:
        return get_sale_data(driver)


def get_sale_data(driver):
    page = BlixSearchPage(driver, url)
    page.open()
    page.wait_for_page_to_load()

    consent_container = ConsentContainerPageObject(driver)
    consent_container.wait_for_object_to_load()
    consent_container.do_not_consent.click()

    page.expand_product_list()
    page.expand_leaflet_list()

    products = list()
    for leaf in page.leaflet_list:
        product = dict(store=leaf.store.text,
                       time=leaf.time.text,
                       url=leaf.leaflet_page.get_attribute('href'),
                       price="N/A",
                       name="N/A")
        products.append(product)

    price_dict = dict()

    for product in page.product_list:
        value = (product.name.text, product.price.text)
        href = product.name.get_attribute('href')
        price_dict[href] = value

    for url_, value in price_dict.items():
        page = BlixProductPage(driver).open(url_)
        page.wait_for_page_to_load()
        for product in products:
            if page.get_leaflet_origin_url() == product["url"]:
                product["name"] = value[0]
                product["price"] = value[1]

    print("PRODUKTY")
    products.sort(key=lambda product: product["name"] == "N/A")
    for p in products:
        print(f"{p['name']}, {p['price']}, {p['store']}, {p['time']}, {p['url']}")

    return products


if __name__ == '__main__':
    get_data()
