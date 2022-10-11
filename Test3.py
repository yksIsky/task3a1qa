from Form.PageDomoQa import PageDemoQa
import pytest
from Form.PageWebtables import WebTables

@pytest.mark.usefixtures("setup")
class Test2():

    def test_no_1(self):
        self.test = PageDemoQa()
        self.test.get_page()
        assert self.test.is_open() == True, 'page is not opened'
        self.test.click_button_elements()
        self.test = WebTables()
        self.test.click_button_web_tables()
        self.test.is_page_web_tables_open()
        self.test.click_button_add()
        self.test.send_value_name(1)
        self.test.send_value_surname(1)
        self.test.send_value_email(1)
        self.test.send_value_age(1)
        self.test.send_value_salary(1)
        self.test.send_value_department(1)
        self.test.click_button_submit()
        assert self.test.is_filled_in(1) == True

    def test_no_2(self):
        self.test = PageDemoQa()
        self.test.get_page()
        assert self.test.is_open() == True, 'page is not opened'
        self.test.click_button_elements()
        self.test = WebTables()
        self.test.click_button_web_tables()
        self.test.is_page_web_tables_open()
        self.test.click_button_add()
        self.test.send_value_name(2)
        self.test.send_value_surname(2)
        self.test.send_value_email(2)
        self.test.send_value_age(2)
        self.test.send_value_salary(2)
        self.test.send_value_department(2)
        self.test.click_button_submit()
        assert self.test.is_filled_in(2) == True

