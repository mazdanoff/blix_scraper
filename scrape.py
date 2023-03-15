from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service

from conf.paths import geckodriver
from conf.urls import SEARCH_PAGE
from page_objects.blix_search_page.blix_search_page import BlixSearchPage
from page_objects.blix_search_page.consent_container_page_object import ConsentContainerPageObject


class Driver:

    def __init__(self):
        self.opts = FirefoxOptions()
        self.service = Service(executable_path=geckodriver)
        self.opts.add_argument("-headless")
        self.driver = None

    def __enter__(self):
        self.driver = Firefox(options=self.opts, service=self.service)
        self.driver.maximize_window()
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self.driver.quit()


phrase = "napój-owsiany"
url = SEARCH_PAGE.format(phrase)

with Driver() as driver:
    page = BlixSearchPage(driver, url)
    page.open()
    page.wait_for_page_to_load()

    consent_container = ConsentContainerPageObject(driver)
    consent_container.wait_for_object_to_load()
    consent_container.do_not_consent.click()

    page.expand_lists()

    print("GAZETKI")
    for leaf in page.leaflet_list:
        print(f"{leaf.store_name.text}, {leaf.time_duration.text}, {leaf.leaflet_page_img.get_attribute('href')}")

    print("PRODUKTY")
    for product in page.product_list:
        print(f"{product.product_name.text}, {product.product_price.text}")
