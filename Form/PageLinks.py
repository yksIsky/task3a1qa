from BaseForm.BaseForm import BaseForm
from Elements.BaseElement import BaseElement
from Utility.logging import logger
from selenium.webdriver.common.by import By
from Elements.Links import Links
from Elements.Button import Button

class PageLinks(BaseForm):

    def __init__(self):
        self.__LINKS_PAGE_LINKS = Links(
        By.XPATH, '//div[@class="main-header" and contains(text(), "Links")]', 'Page Links')
        self.__BUTTON_HOME = Button(By.XPATH, '//a[@id="simpleLink" and contains(text(), "Home")]', 'Button Home')

    def is_page_links_open(self):
        logger.info(f'Checkin is page opened {self.__LINKS_PAGE_LINKS.name}')
        return self.__LINKS_PAGE_LINKS.is_displayed()

    def click_button_home(self):
        logger.info(f'clicking button {self.__BUTTON_HOME.name}')
        self.__BUTTON_HOME.force_click()
