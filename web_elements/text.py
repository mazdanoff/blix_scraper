from web_elements.element import Element


class Text(Element):

    @property
    def text(self):
        return self.element.text
