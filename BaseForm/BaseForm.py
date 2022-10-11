
from Utility.logging import logger
from abc import ABC
from Utility.DataUtility import Data
from Elements.UniqueElement import UniqueElement


class BaseForm(ABC):

    def __init__(self, by_: str, unique_element: str):
        self.page: str = Data.data_access(f"{chr(92)}ConfigData.json", "URL", "pageName", 1)
        self.__Unique_element = UniqueElement(by_, unique_element, self.page)

    def is_open(self):
        logger.info(f'is page opened {self.__Unique_element.name}')
        return self.__Unique_element.is_displayed()




