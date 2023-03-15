from selenium_datatable import DataTable, Column

from .blix_search_page_locators import BlixSearchPageLocators as Loc


class LeafletList(DataTable):

    rows_locator = Loc.LEAFLET_CONTAINER
    headers_locator = Loc.LEAFLETS_SECTION

    store_name = Column(*Loc.STORE_NAME)
    time_duration = Column(*Loc.TIME_DURATION)
    leaflet_page_img = Column(*Loc.LEAFLET_PAGE_IMG)
