from Elements.BaseElement import BaseElement


class NestedFramesElement(BaseElement):

    def __init__(self, by_: str, locator: str, name: str):
        super(NestedFramesElement, self).__init__(by_, locator, name)

