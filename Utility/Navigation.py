from Elements.BaseElement import BaseElement
from abc import abstractclassmethod, ABC
from Utility.Driver import BrowserUtils
from Utility.logging import logger
from Utility.Wait import Wait
from selenium.webdriver.support import expected_conditions as EC


class Navigation(BaseElement):

    @staticmethod
    def back():
        logger.info(f'page back')
        BrowserUtils.return_instance().back()

    @staticmethod
    def forward():
        logger.info(f'page forward')
        BrowserUtils.return_instance().forward()

    @staticmethod
    def refresh():
        logger.info(f'page refresh')
        BrowserUtils.return_instance().refresh()

    @staticmethod
    def set_window():
        logger.info(f'saving oryginal window name')
        original_window = BrowserUtils.return_instance().current_window_handle
        return original_window

    @staticmethod
    def switch_window_new( window: str):
        logger.info(f'change window to new ')
        Wait.wait().until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != window:
                BrowserUtils.return_instance().switch_to.window(window_handle)
                break

    @staticmethod
    def switch_window_oryginal( window: str):
        logger.info(f'change window to oryginal ')
        Wait.wait().until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle == window:
                BrowserUtils.return_instance().switch_to.window(window_handle)
                break

    @staticmethod
    def switch_tab_new( window: str):
        logger.info(f'change tab  to new ')
        Wait.wait().until(EC.number_of_windows_to_be(2))
        BrowserUtils.return_instance().switch_to.window(BrowserUtils.return_instance().window_handles[1])

    @staticmethod
    def switch_tab_oryginal( window: str):
        logger.info(f'change tab  to oryginal ')
        BrowserUtils.return_instance().switch_to.window(BrowserUtils.return_instance().window_handles[0])

    @staticmethod
    def close_tab():
        logger.info(f'closing current tab')
        BrowserUtils.return_instance().close()
