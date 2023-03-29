from dataclasses import dataclass


@dataclass
class SaleData:
    """Class for combined leaflet/product data"""
    name: str
    price: str
    store: str
    time: str
    link_to_img: str
    leaflet_link: str

    def __str__(self):
        return "{name}, {price} zł\n{time} in {store}\n{img_url}".format(
            name=self.name,
            price=self.price,
            time=self.time,
            store=self.store,
            img_url=self.link_to_img
        )


@dataclass
class LeafletData:
    """Class for data scraped from leaflet list"""
    store: str
    time: str
    leaflet_link: str

    def __str__(self):
        return f"LEAFLET: {self.leaflet_link}, {self.store}, {self.time}"


@dataclass
class ProductData:
    """Class for data scraped from product page"""
    name: str
    price: str
    store: str
    link_to_img: str
    leaflet_link: str

    def __str__(self):
        return "{name}, {price} zł\nin {store}\n{img_url}".format(
            name=self.name,
            price=self.price,
            store=self.store,
            img_url=self.link_to_img
        )
