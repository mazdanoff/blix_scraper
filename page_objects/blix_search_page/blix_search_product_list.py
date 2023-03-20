from selenium_datatable import DataTable, Column

from .blix_search_page_locators import BlixSearchPageLocators as Loc


class ProductList(DataTable):

    rows_locator = Loc.PRODUCT_CONTAINER
    headers_locator = Loc.PRODUCTS_SECTION

    name = Column(*Loc.PRODUCT_NAME)
    price = Column(*Loc.PRODUCT_PRICE)
