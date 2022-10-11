from abc import abstractclassmethod, ABC
from Utility.DataUtility import Data
from selenium.webdriver.support.ui import WebDriverWait
from Utility.logging import logger
from Utility.Driver import BrowserUtils


class Wait():

    @abstractclassmethod
    def wait(cls):
        time = int(Data.data_access(f"{chr(92)}TestData.json",'Wait','Wait', 1))
        logger.info(f"setting wait time to {time}")
        wait = WebDriverWait(BrowserUtils.return_instance(), int(Data.data_access("\TestData.json",'Wait','Wait', 1)))
        return wait


