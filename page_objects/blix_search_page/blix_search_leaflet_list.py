from selenium_datatable import DataTable, Column

from .blix_search_page_locators import BlixSearchPageLocators as Loc


class LeafletList(DataTable):

    rows_locator = Loc.LEAFLET_CONTAINER
    headers_locator = Loc.LEAFLETS_SECTION

    store = Column(*Loc.STORE_NAME)
    time = Column(*Loc.TIME_DURATION)
    leaflet_page = Column(*Loc.LEAFLET_PAGE_IMG)
