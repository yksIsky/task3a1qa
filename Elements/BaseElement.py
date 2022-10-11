from abc import abstractclassmethod, ABC
from Utility.Driver import BrowserUtils
from Utility.logging import logger
from selenium.webdriver.support import expected_conditions as EC
from Utility.Wait import Wait
from selenium.webdriver.common.by import By


class BaseElement(ABC):

    def __init__(self, by_: str, locator: str, name: str):
        self.by_ = by_
        self.locator = locator
        self.name = name

    def find_element(self):
        logger.info(f'finding the element {self.name}')
        return BrowserUtils.return_instance().find_element(self.by_, self.locator)

    def clicks(self):
        return self.find_element().click()

    def force_click(self):
        logger.info(f'force click {self.name}')
        element = Wait.wait().until(EC.presence_of_element_located((self.by_, self.locator)))
        return BrowserUtils.return_instance().execute_script("arguments[0].click();", element)

    def is_displayed(self):
        logger.info(f'is displayed the element {self.name}')
        return Wait.wait().until(EC.presence_of_element_located((self.by_, self.locator))).is_displayed()

    def is_it_displayed(self, par: str):
        logger.info(f'is displayed the element {self.name}')
        return Wait.wait().until(EC.presence_of_element_located((self.by_, f'{self.locator}{par}")]'))).is_displayed()

    def get(self):
        logger.info(f'getting the element {self.name}')
        return BrowserUtils.return_instance().get(self.locator)
