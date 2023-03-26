from selenium.webdriver.common.by import By


class BlixProductPageLocators:

    PRODUCT_NAME = (By.CSS_SELECTOR, "h1.top-wrapper__product-title")
    STORE_NAME = (By.CSS_SELECTOR, "span.brand-name")
    PRICE = (By.CSS_SELECTOR, "span.price-value")
    LEAFLET_IMG = (By.CSS_SELECTOR, "div.swiper-slide-active div.page-wrapper img")
    LEAFLET_LINK = (By.CSS_SELECTOR, "a.ga-product-leaflet-link")
