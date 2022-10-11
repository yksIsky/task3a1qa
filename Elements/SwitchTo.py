from Elements.BaseElement import BaseElement
from abc import abstractclassmethod, ABC
from Utility.Driver import BrowserUtils
from Utility.logging import logger
from selenium.webdriver.support import expected_conditions as EC
from Utility.Wait import Wait


class Frames(BaseElement):

    def __init__(self, by_: str, locator: str, name: str):
        super(Frames, self).__init__(by_, locator, name)


    def switch_frame(self):
        logger.info(f'choosing frame {self.name}')
        frames = Wait.wait().until(EC.presence_of_element_located((self.by_, self.locator)))
        BrowserUtils.return_instance().switch_to.frame(frames)

    def switch_default_content(self):
        logger.info(f'return default frame')
        BrowserUtils.return_instance().switch_to.default_content()
