from web_elements.element import Element


class Link(Element):

    def click(self):
        self.element.click()

    @property
    def text(self):
        return self.element.text

    @property
    def link(self):
        return self.element.get_attribute("href")
