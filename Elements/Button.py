from Elements.BaseElement import BaseElement


class Button(BaseElement):

    def __init__(self, by_: str, locator: str, name: str):
        super(Button, self).__init__(by_, locator, name)

