from BaseForm.BaseForm import BaseForm
from Elements.BaseElement import BaseElement
from Utility.logging import logger
from selenium.webdriver.common.by import By
from Elements.Button import Button
from Elements.SwitchTo import Frames
from Elements.Labels import Labels
from Elements.NestedFrames import NestedFramesElement

class NestedFrames(BaseForm):

    def __init__(self):
        self.__BUTTON_NASTED_FRAMES = Button(
            By.XPATH, '//span[@class="text" and contains(text(),"Nested Frames")]', 'Button NESTED FRAMES')


        self.__READ_LABLES_PARENT_FRAME = Labels(By.XPATH, '//body[contains(text(), "Parent frame")]', 'Parent Frame text')
        self.__READ_LABLES_CHILD_FRAME = Labels(By.XPATH, '//*[contains(text(), "Child Iframe")]', 'Child Iframe text')
        self.__NESTED_FRAME_IS_NESTED_FRAMES = NestedFramesElement(By.XPATH, '//div[@class="main-header" and contains(text(),"Nested Frames")]', 'Nasted frame')

    def click_button_nested_frames(self):
        logger.info(f'clicking button {self.__BUTTON_NASTED_FRAMES.name}')
        return self.__BUTTON_NASTED_FRAMES.force_click()

    def is_page_nested_frames_changed_parent(self):
        logger.info(f'switching to ifeame {self.__READ_LABLES_PARENT_FRAME.name}')
        return self.__READ_LABLES_PARENT_FRAME.read_labels()

    def is_page_nested_frames_changed_child(self):
        logger.info(f'switching to ifeame {self.__READ_LABLES_CHILD_FRAME.name}')
        return self.__READ_LABLES_CHILD_FRAME.read_labels()



    def is_nested_frames_opened(self):
        logger.info(f'Checkin is page opened {self.__NESTED_FRAME_IS_NESTED_FRAMES.name}')
        return self.__NESTED_FRAME_IS_NESTED_FRAMES.is_displayed()
