from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service

from conf.paths import geckodriver
from conf.urls import SEARCH_PAGE
from page_objects.blix_search_page.blix_product_page import BlixProductPage
from page_objects.blix_search_page.blix_search_page import BlixSearchPage
from page_objects.blix_search_page.consent_container_page_object import ConsentContainerPageObject


class Driver:

    def __init__(self):
        self.driver = None
        self.opts = FirefoxOptions()
        self.service = Service(executable_path=geckodriver)
        self.opts.add_argument("-headless")

    def __enter__(self):
        self.driver = Firefox(options=self.opts, service=self.service)
        self.driver.maximize_window()
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self.driver.quit()


# phrase = "napój-owsiany"
phrase = "ser-mozzarella"
url = SEARCH_PAGE.format(phrase)

with Driver() as driver:
    page = BlixSearchPage(driver, url)
    page.open()
    page.wait_for_page_to_load()

    consent_container = ConsentContainerPageObject(driver)
    consent_container.wait_for_object_to_load()
    consent_container.do_not_consent.click()

    page.expand_product_list()
    page.expand_leaflet_list()

    # for leaflet in page.leaflet_list:
    #     print(f"{leaflet.store.text}, {leaflet.time.text}, {leaflet.leaflet_page.get_attribute('href')}")

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

    for url, value in price_dict.items():
        page = BlixProductPage(driver).open(url)
        page.wait_for_page_to_load()
        for product in products:
            if page.get_leaflet_origin_url() == product["url"]:
                product["name"] = value[0]
                product["price"] = value[1]

    print("PRODUKTY")
    products.sort(key=lambda product: product["name"] == "N/A")
    for p in products:
        print(f"{p['name']}, {p['price']}, {p['store']}, {p['time']}, {p['url']}")
