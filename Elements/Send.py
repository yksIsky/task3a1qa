from Elements.BaseElement import BaseElement
from abc import abstractclassmethod, ABC
from Utility.Driver import BrowserUtils
from Utility.logging import logger

class Send(BaseElement):


    def __init__(self, by_: str, locator: str, name: str):
        super(Send, self).__init__(by_, locator, name)

    def send(self,value):
        logger.info(f'send value  {self.name}')
        BrowserUtils.return_instance().find_element(self.by_, self.locator).send_keys(value)
