from BaseForm.BaseForm import BaseForm
from Elements.BaseElement import BaseElement
from Utility.logging import logger
from selenium.webdriver.common.by import By
from Elements.Alerts import Alerts
from Elements.Random import random_name
from Utility.DataUtility import Data
from Elements.Button import Button
from Elements.Alerts import Alerts
from Elements.Labels import Labels

class PageAlerts(BaseForm):

    def __init__(self):
        self.__BUTTON_ALERTS = Button(
            By.XPATH, '//li[@id="item-1"]//span[@class="text" and contains(text(),"Alerts")]', 'Button Alerts')
        self.__LABLES_HEADER_ALERTS = Labels(
            By.XPATH, '//div[@class="main-header" and contains(text(),"Alerts")]', 'Heder Alerts')
        self.__BUTTON_TO_SEE_ALERT = Button(
            By.XPATH, '//button[@id="alertButton"]', 'Button Click Button to see alert')
        self.__ALERT_CLICK_BUTTON = Alerts(" ", " ", 'click button')

        self.__BUTTON_CONFIRM_BOX = Alerts(By.XPATH, '//button[@id="confirmButton"]', 'confirm box ')
        self.__READ_LABLES_YOU_SELECTED_OK = Labels(
            By.XPATH, '//span[@id="confirmResult" and contains(text(),"You selected")]', 'You selected Ok')
        self.__Button_PROMPT_BOX = Button(By.XPATH, '//button[@id="promtButton"]', 'Button prompt box')
        self.__ALLERT_PROMPT_BOX = Alerts('','','Button prompt box')
        self.__READ_LABLES_PROPMPT_NAME = Labels(By.XPATH, '//*[@id="promptResult"]', 'input name')

    def click_button_alerts(self):
        logger.info(f'clicking button {self.__BUTTON_ALERTS.name}')
        self.__BUTTON_ALERTS.force_click()

    def is_alerts_clicked(self):
        logger.info(f'Checkin is page opened with {self.__LABLES_HEADER_ALERTS.name}')
        return self.__LABLES_HEADER_ALERTS.read_labels()

    def click_Button_To_See_Alert(self):
        logger.info(f'clicking button {self.__BUTTON_TO_SEE_ALERT.name}')
        self.__BUTTON_TO_SEE_ALERT.force_click()

    def is_alert_open(self):
        logger.info(f'checking is allert opened')
        return self.__ALERT_CLICK_BUTTON.is_alert_displayed()

    def accept_allert(self):
        logger.info(f'acepting allert {self.__ALERT_CLICK_BUTTON.name}')
        self.__ALERT_CLICK_BUTTON.alert_accept()

    def click_confirm_box(self):
        logger.info(f'clicking button {self.__BUTTON_CONFIRM_BOX.name}')
        self.__BUTTON_CONFIRM_BOX.force_click()

    def is_alert_open_confirm_box(self):
        logger.info(f'checking is allert opened {self.__BUTTON_CONFIRM_BOX.name}')
        return self.__BUTTON_CONFIRM_BOX.is_alert_displayed()

    def is_dislayed_you_selected_ok(self):
        logger.info(f'Checkin is page opened {self.__READ_LABLES_YOU_SELECTED_OK.name}')
        return self.__READ_LABLES_YOU_SELECTED_OK.read_labels()

    def click_prompt_box(self):
        logger.info(f'clicking button {self.__Button_PROMPT_BOX.name}')
        self.__Button_PROMPT_BOX.force_click()

    def is_alert_open_please_enter_your_name(self):
        logger.info(f'checking is allert opened {self.__ALLERT_PROMPT_BOX.name}')
        return self.__ALLERT_PROMPT_BOX.is_alert_displayed()

    def send_input_prompt_box(self, name:str):
        logger.info(f'generatting new name {self.__ALLERT_PROMPT_BOX.name}')
        self.__ALLERT_PROMPT_BOX.alert_input(name)

    def is_name_correct(self):
        logger.info(f'read name from {self.__READ_LABLES_PROPMPT_NAME.name}')
        return self.__READ_LABLES_PROPMPT_NAME.read_labels()
