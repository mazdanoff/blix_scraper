from web_elements.element import Element


class Image(Element):

    @property
    def src(self):
        return self.element.get_attribute('src')
