from BaseForm.BaseForm import BaseForm

from Utility.logging import logger
from selenium.webdriver.common.by import By
from Elements.Send import Send
from Elements.Button import Button
from Elements.OsElement import OsFile
from pathlib import Path
from Elements.Labels import Labels
import os

class PageUploadDownload(BaseForm):

    def __init__(self):

        self.__BUTTON_UPLOAD = Button(By.XPATH, '//li[@id="item-7"]', 'Button Upload')
        self.__BUTTON_IS_DOWNLOAD = Button(By.XPATH, '//a[@class="btn btn-primary"]', 'Button Is Download')
        self.__BUTTON_DOWNLOAD = Button(By.XPATH, '//a[@class="btn btn-primary"]', 'Button Upload')
        self.__FILE_EXIST = OsFile(By.XPATH, '//a[@class="btn btn-primary"]', 'File')
        self.__BUTTON_CHOOSE_FILE = Send(By.XPATH, '//input[@id = "uploadFile"]', 'Choose File')
        self.__READ_LEABLE_FILE_NAME = Labels(By.XPATH, '//p[@id="uploadedFilePath" and contains(text(), "sampleFile")]', "Read file name")

    def click_button_upload(self):
        logger.info(f'clicking button {self.__BUTTON_UPLOAD.name}')
        self.__BUTTON_UPLOAD.force_click()

    def is_open_page_upload(self):
        logger.info(f'clicking button {self.__BUTTON_IS_DOWNLOAD.name}')
        return self.__BUTTON_IS_DOWNLOAD.is_displayed()

    def click_button_download(self):
        logger.info(f'clicking button {self.__BUTTON_DOWNLOAD.name}')
        self.__BUTTON_DOWNLOAD.force_click()

    def is_file_exists(self):
        logger.info(f'is download file exists')
        return self.__FILE_EXIST.is_file_exists()

    def click_button_choose_file(self):
        logger.info(f'clicking button {self.__BUTTON_CHOOSE_FILE.name}')
        filepath_real = Path(os.path.dirname(os.path.realpath(__file__)))
        script_dir = str(filepath_real.parent)
        file_path = f'{script_dir}\sampleFile.jpeg'
        self.__BUTTON_CHOOSE_FILE.send(file_path)

    def is_uploded(self):
        logger.info(f'check is  {self.__READ_LEABLE_FILE_NAME.name}')
        return self.__READ_LEABLE_FILE_NAME.is_displayed()
