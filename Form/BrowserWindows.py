from BaseForm.BaseForm import BaseForm
from Elements.BaseElement import BaseElement
from Utility.logging import logger
from selenium.webdriver.common.by import By
from Utility.Navigation import Navigation
from Elements.Button import Button
from Elements.SwitchTo import Frames
from Elements.Labels import Labels
from Elements.NestedFrames import NestedFramesElement


class BrowserWindows(BaseForm):

    def __init__(self):
        self.__BUTTON_BROWSER_WINDOWS = Button(
            By.XPATH, '//li[@id="item-0"]//span[@class="text" and contains(text(),"Browser Windows")]',
            'Browser Windows')

        self.__BUTTON_NEW_TAB = Button(By.XPATH, '//button[@id="tabButton"]', 'New Tab')




        self.__IS_BUTTON_NEW_TAB_OPEN = Button(By.XPATH, '//h1[@id="sampleHeading"]', 'is open new tab')

        self.__BUTTON_CLICK_LINKS = Button(
            By.XPATH, '//li[@id="item-5"]//span[@class="text" and contains(text(),"Links")]', 'Elements')

    def click_browser_windows(self):
        logger.info(f'clicking button {self.__BUTTON_BROWSER_WINDOWS.name}')
        self.__BUTTON_BROWSER_WINDOWS.force_click()

    def is_button_new_tab(self):
        logger.info(f'check is button  {self.__BUTTON_NEW_TAB.name}')
        return self.__BUTTON_NEW_TAB.is_displayed()

    def click_new_tab(self):
        logger.info(f'clicking button {self.__BUTTON_NEW_TAB.name}')
        self.__BUTTON_NEW_TAB.force_click()

    def save_tab_name(self):
        logger.info(f'saving tab name')
        Navigation.set_window()

    def switch_tab_new(self, name: str):
        logger.info(f'switch tab tab name')
        Navigation.switch_tab_new(name)

    def switch_tab_oryginal(self, name: str):
        logger.info(f'switch tab tab name')
        Navigation.switch_tab_oryginal(name)

    def close_tab(self):
        logger.info(f'close tab')
        Navigation.close_tab()

    def is_open_new_tab(self):
        logger.info(f'check  {self.__IS_BUTTON_NEW_TAB_OPEN.name}')
        return self.__IS_BUTTON_NEW_TAB_OPEN.is_displayed()

    def click_elements(self):
        logger.info(f'clicking button {self.__BUTTON_CLICK_LINKS.name}')
        self.__BUTTON_CLICK_LINKS.force_click()
