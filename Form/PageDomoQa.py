from BaseForm.BaseForm import BaseForm
from Utility.logging import logger
from selenium.webdriver.common.by import By
from Elements.Button import Button
from Utility.DataUtility import Data

class PageDemoQa(BaseForm):

    def __init__(self):
        super().__init__(By.XPATH, '//img[@class="banner-image" and @alt="Selenium Online Training"]')
        self.URL = Button("By.URL", Data.data_access(f"{chr(92)}ConfigData.json", "URL", "url", 1), "Main page")
        self.id = None
        self.__BUTTON_ALERTS_FRAME_WINDOWS = Button(By.XPATH, '//h5[text()="Alerts, Frame & Windows" ]//parent::div[@class="card-body"]','Button Alerts, Frame & Windows')
        self.__BUTTON_NASTED_FRAMES = Button(
            By.XPATH, '//span[@class="text" and contains(text(),"Nested Frames")]', 'Button NESTED FRAMES')
        self.__BUTTON_XPATH_ELEMENTS = Button(
            By.XPATH, '//h5[text()="Elements" ]//parent::div[@class="card-body"]', 'Button Elements')
        self.__BY_XPATH_BUTTON_WEB_TABLES = (
            By.XPATH, '//li[@id="item-3"]//span[@class="text" and contains(text(),"Web Tables")]', 'Web Tables')

    def get_page(self):
        logger.info(f'opening main page ')
        self.URL.get()

    def is_open(self):
        logger.info(f'Checkin is page opened ')
        return super().is_open()

    def click_button_alerts_frame_windows(self):
        logger.info(f'clicking button {self.__BUTTON_ALERTS_FRAME_WINDOWS.name}')
        self.__BUTTON_ALERTS_FRAME_WINDOWS.force_click()

    def click_button_elements(self):
        logger.info(f'clicking button {self.__BUTTON_XPATH_ELEMENTS.name}')
        self.__BUTTON_XPATH_ELEMENTS.force_click()

'''
    def click_button_nested_frames(self):
        logger.info(f'clicking button {self.__BUTTON_NASTED_FRAMES.name}')
        self.__BUTTON_NASTED_FRAMES.force_click()

'''
