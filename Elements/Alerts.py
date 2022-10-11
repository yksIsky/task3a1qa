from Elements.BaseElement import BaseElement
from abc import abstractclassmethod, ABC
from Utility.Driver import BrowserUtils
from Utility.logging import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utility.Wait import Wait

class Alerts(BaseElement):


    def __init__(self, by_: str, locator: str, name: str):
        super(Alerts, self).__init__(by_, locator, name)

    def switch_to_alert(self):
        Wait.wait().until(EC.alert_is_present())
        return BrowserUtils.return_instance().switch_to.alert


    def is_alert_displayed(self):
        logger.info(f'checking is element poped up {self.name} to see alert ')
        return self.switch_to_alert().text


    def alert_accept( self):
        logger.info(f'acepting allert {self.name} ')
        self.switch_to_alert().accept()


    def alert_input( self, input):
        logger.info(f'creating input {self.name} ')
        self.switch_to_alert
        return self.switch_to_alert().send_keys(input)