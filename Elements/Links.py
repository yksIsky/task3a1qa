from Elements.BaseElement import BaseElement


class Links(BaseElement):

    def __init__(self, by_: str, locator: str, name: str):
        super(Links, self).__init__(by_, locator, name)

