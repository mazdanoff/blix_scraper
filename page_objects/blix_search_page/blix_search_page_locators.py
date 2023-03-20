from selenium.webdriver.common.by import By


class BlixSearchPageLocators:

    LEAFLET_COUNT = (By.CSS_SELECTOR, ".Section > section:nth-of-type(2) > h2 > span")
    LEAFLETS_SECTION = (By.CSS_SELECTOR, ".section-vc__items--leaflets")
    LEAFLET_CONTAINER = (By.CSS_SELECTOR, ".section__item--cell.leaflet")
    LEAFLET_EXPAND_BUTTON = (By.CSS_SELECTOR, "section.last-section button.button.expand-section")
    STORE_NAME = (By.CSS_SELECTOR, "div.section__item.leaflet:nth-of-type({row}) .leaflet__info-texts > h5")
    TIME_DURATION = (By.CSS_SELECTOR, "div.section__item.leaflet:nth-of-type({row}) .leaflet__duration > strong")
    LEAFLET_PAGE_IMG = (By.CSS_SELECTOR, "div.section__item.leaflet:nth-of-type({row}) .leaflet__info-texts > a")

    PRODUCT_COUNT = (By.CSS_SELECTOR, ".Section > section:nth-of-type(3) > h2 > span")
    PRODUCTS_SECTION = (By.CSS_SELECTOR, ".section-vc__items--products")
    PRODUCT_CONTAINER = (By.CSS_SELECTOR, ".section__item.similar-product")
    PRODUCT_EXPAND_BUTTON = (By.CSS_SELECTOR, "section.sortable button.button.expand-section")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.section__item.similar-product:nth-of-type({row}) h6.similar-product__name > a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.section__item.similar-product:nth-of-type({row}) span.similar-product__price")
