from BaseForm.BaseForm import BaseForm
from Elements.BaseElement import BaseElement
from Utility.logging import logger
from selenium.webdriver.common.by import By
from Utility.DataUtility import Data
from Elements.Send import Send
from Elements.Button import Button
from Elements.UniqueElement import UniqueElement

class WebTables(BaseForm):

    def __init__(self):
        super().__init__(By.XPATH, '//div[@class="main-header" and contains(text(),"Web Tables")]')
        self.__BUTTON_WEB_TABLES = Button(
            By.XPATH, '//li[@id="item-3"]//span[@class="text" and contains(text(),"Web Tables")]', 'Web Tables')
        self.__BUTTON_ADD = Button(By.XPATH, '//button[@id="addNewRecordButton"]', 'Button ADD')


        self.__SEND_FIRST_NAME = Send(By.XPATH, '//input[@id="firstName"]', 'name')

        self.__SEND_LAST_NAME = Send(By.XPATH, '//input[@id="lastName"]', 'lastName')
        self.__SEND_EMAIL = Send(By.XPATH, '//input[@id="userEmail"]', 'email')
        self.__SEND_AGE = Send(By.XPATH, '//input[@id="age"]', 'age')
        self.__SEND_SALARY = Send(By.XPATH, '//input[@id="salary"]', 'salary')
        self.__SEND_DEPARTMENT = Send(By.XPATH, '//input[@id="department"]', 'department')
        self.__BUTTON_SUBMIT_BUTTON = Button(By.XPATH, '//button[@id="submit"]', 'Button Submit')
        self.__UNIQUE_ELEMENT_CHECK_NAME = UniqueElement(By.XPATH, '//div[@class="rt-td"  and contains(text(),"', f'Check values')

    def click_button_web_tables(self):
        logger.info(f'clicking button {self.__BUTTON_WEB_TABLES.name}')
        self.__BUTTON_WEB_TABLES.force_click()

    def is_page_web_tables_open(self):
        logger.info(f'Checkin is page opened')
        return super().is_open()

    def click_button_add(self):
        logger.info(f'clicking button {self.__BUTTON_ADD.name}')
        self.__BUTTON_ADD.force_click()

    def send_value_name(self, id:str):
        logger.info(f'filling in {self.__SEND_FIRST_NAME.name}')
        self.__SEND_FIRST_NAME.send( id)

    def send_value_surname(self, id:str):
        logger.info(f'filling in {self.__SEND_LAST_NAME.name}')
        self.__SEND_LAST_NAME.send(  id)

    def send_value_email(self, id:str):
        logger.info(f'filling in {self.__SEND_EMAIL.name}')
        self.__SEND_EMAIL.send(  id)

    def send_value_age(self, id:str):
        logger.info(f'filling in {self.__SEND_AGE.name}')
        self.__SEND_AGE.send(  id)

    def send_value_salary(self, id:str):
        logger.info(f'filling in {self.__SEND_SALARY.name}')
        self.__SEND_SALARY.send(  id)

    def send_value_department(self, id:str):
        logger.info(f'filling in {self.__SEND_DEPARTMENT.name}')
        self.__SEND_DEPARTMENT.send( id)

    def click_button_submit(self):
        logger.info(f'clicking button {self.__BUTTON_SUBMIT_BUTTON.name}')
        self.__BUTTON_SUBMIT_BUTTON.force_click()

    def is_send_value_name(self, id:str):
        logger.info(f'filling in {self.__SEND_FIRST_NAME.name}')

    def is_send_value_surname(self, id:str):
        logger.info(f'filling in {self.__SEND_LAST_NAME.name}')
        self.__UNIQUE_ELEMENT_CHECK_NAME.is_it_displayed(id)

    def is_send_value_email(self, id:str):
        logger.info(f'filling in {self.__SEND_EMAIL.name}')
        self.__UNIQUE_ELEMENT_CHECK_NAME.is_it_displayed(id)

    def is_send_value_age(self, id:str):
        logger.info(f'filling in {self.__SEND_AGE.name}')
        self.__UNIQUE_ELEMENT_CHECK_NAME.is_it_displayed(id)

    def is_send_value_salary(self, id:str):
        logger.info(f'filling in {self.__SEND_SALARY.name}')
        self.__UNIQUE_ELEMENT_CHECK_NAME.is_it_displayed(id)

    def is_send_value_department(self, id:str):
        logger.info(f'filling in {self.__SEND_DEPARTMENT.name}')
        self.__UNIQUE_ELEMENT_CHECK_NAME.is_it_displayed(id)

    def is_click_button_submit(self):
        logger.info(f'clicking button {self.__BUTTON_SUBMIT_BUTTON.name}')
        self.__BUTTON_SUBMIT_BUTTON.force_click()
