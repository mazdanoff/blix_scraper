from dataclasses import dataclass


@dataclass
class SaleData:
    name: str
    price: str
    store: str
    time: str
    link_to_img: str
    leaflet_link: str

    def __str__(self):
        return f"SALE: {self.leaflet_link}, {self.name}, {self.price}, {self.store}, {self.time}, {self.link_to_img}"


@dataclass
class LeafletData:
    store: str
    time: str
    leaflet_link: str

    def __str__(self):
        return f"LEAFLET: {self.leaflet_link}, {self.store}, {self.time}"


@dataclass
class ProductData:
    name: str
    price: str
    store: str
    link_to_img: str
    leaflet_link: str

    def __str__(self):
        return f"PRODUCT: {self.leaflet_link}, {self.name}, {self.price}, {self.store}, {self.link_to_img}"
