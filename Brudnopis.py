from abc import abstractclassmethod, ABC
from Utility.Driver import BrowserUtils
from Utility.logging import logger
from selenium.webdriver.support import expected_conditions as EC
from Utility.Wait import Wait
from selenium.webdriver.common.by import By




class BaseElement(ABC):

    def __init__(self, by_:str,locator:str,name:str):
        self.by_ = by_
        self.locator = locator
        self.name = name



    def find_element(self):
        logger.info(f'finding the element {self.name}')
        return BrowserUtils.return_instance().find_element(self.by_, self.locator)

    def clicks(self):

       return self.find_element().click()


class Button(BaseElement):

    def __init__(self,  by_:str,locator:str,name:str):
        super(Button, self).__init__(by_, locator, name)


class Page1():

    def __init__(self):
        self.__x = Button(By.XPATH, '//*[@id="L2AGLb"]/div',
                   'Button Alerts, Frame & Windows')

    def get(self):
        BrowserUtils.return_instance().get('https://www.google.com/')

    def button_click(self):
        self.__x.clicks()

z = Page1()
z.get()
z.button_click()
