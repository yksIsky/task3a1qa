from Elements.BaseElement import BaseElement


class UniqueElement(BaseElement):

    def __init__(self, by_: str, locator: str, name: str):
        super(UniqueElement, self).__init__(by_, locator, name)