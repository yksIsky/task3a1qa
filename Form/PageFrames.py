from BaseForm.BaseForm import BaseForm
from Utility.logging import logger
from selenium.webdriver.common.by import By
from Utility.Navigation import Navigation
from Elements.Button import Button
from Elements.SwitchTo import Frames
from Elements.Labels import Labels


class Frame(BaseForm):

    def __init__(self):
        super().__init__(By.XPATH, '//div[@class="main-header" and contains(text(),"Frames")]')
        self.__BUTTON_FRAMES = Button(By.XPATH, '//span[@class="text" and contains(text(),"Frames")]', 'Button Frames')
        self.__FRAME_PAGE_FRAME_TOP = Frames(By.XPATH, f'//iframe[@id="frame1"]', 'changing to frame1')
        self.__FRAME_PAGE_FRAME_BOT = Frames(By.XPATH, f'//iframe[@id="frame2"]', 'changing to frame2')
        self.__FRAME_PAGE_FRAME_CHILD = Frames(
            By.XPATH, f'//iframe[@srcdoc = "<p>Child Iframe</p>"]', 'changing to frame child')
        self.__TEXT_FRAME_NAME = Labels(
            By.XPATH, '//h1[@id="sampleHeading" and contains(text(),"This is a sample page")]', 'Frame name')

    def get_page(self):
        super().get_page()

    def is_frames_opened(self):
        logger.info(f'Checkin is page opened')
        return super().is_open()

    def click_button_frames(self):
        logger.info(f'clicking button {self.__BUTTON_FRAMES.name}')
        self.__BUTTON_FRAMES.force_click()

    def switch_frames_top(self):
        logger.info(f'read frame one name {self.__FRAME_PAGE_FRAME_TOP.name}')
        self.__FRAME_PAGE_FRAME_TOP.switch_frame()

    def swtich_frames_bot(self):
        logger.info(f'read frame one name {self.__FRAME_PAGE_FRAME_BOT.name}')
        self.__FRAME_PAGE_FRAME_BOT.switch_frame()

    def swtich_frames_child(self):
        logger.info(f'read frame one name {self.__FRAME_PAGE_FRAME_CHILD.name}')
        self.__FRAME_PAGE_FRAME_CHILD.switch_frame()

    def switch_defoult(self):
        logger.info('Checkin is page opened defoult')
        self.__FRAME_PAGE_FRAME_TOP.switch_default_content()

    def page_refres(self):
        logger.info(f'refreshihng page')
        Navigation.refresh()

    def is_frame_correct(self):
        logger.info(f'read frame one name {self.__TEXT_FRAME_NAME.name}')
        self.page_refres()
        self.switch_defoult()
        self.switch_frames_top()
        self.top_frame = self.__TEXT_FRAME_NAME.read_labels()
        self.page_refres()
        self.swtich_frames_bot()
        self.bot_frame = self.__TEXT_FRAME_NAME.read_labels()
        if self.top_frame == self.bot_frame:
            return True
