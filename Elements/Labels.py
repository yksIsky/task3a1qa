from Elements.BaseElement import BaseElement
from Utility.logging import logger


class Labels(BaseElement):

    def __init__(self, by_: str, locator: str, name: str):
        super(Labels, self).__init__(by_, locator, name)


    def read_labels(self):
        logger.info(f'check is data was correctly filled in {self.name}')
        return self.find_element().text

