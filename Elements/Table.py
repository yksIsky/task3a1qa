from Elements.BaseElement import BaseElement
from abc import abstractclassmethod, ABC
from Utility.Driver import BrowserUtils
from Utility.logging import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utility.Wait import Wait

class Table(BaseElement):

    def __init__(self, by_: str, locator: str, name: str):
        super(Table, self).__init__(by_, locator, name)