from Form.PageDomoQa import PageDemoQa
import softest
import pytest
from Utility.DataUtility import Data
from Form.PageWebtables import WebTables
from Form.BrowserWindows import BrowserWindows
from Form.PageUploadDownload import PageUploadDownload
from Form.PageLinks import PageLinks
from Form.PageAlerts import PageAlerts
from Form.PageNestedFrames import NestedFrames
from Form.PageFrames import Frame
from Elements.Random import random_name
from ddt import ddt, file_data
from Utility.Fixture import setup


@pytest.mark.usefixtures("setup")
@ddt
class Test3(softest.TestCase):

    @file_data('./Data/ddt1.json')
    def test_no(self, name, surname, email, age, salary, department):
        self.PageDemoQa = PageDemoQa()
        self.PageDemoQa.get_page()
        assert self.PageDemoQa.is_open() == True, 'page is not opened'
        self.PageDemoQa.click_button_elements()
        self.WebTables = WebTables()
        self.WebTables.click_button_web_tables()
        self.WebTables.is_page_web_tables_open()
        self.WebTables.click_button_add()
        self.WebTables.send_value_name(name)
        self.WebTables.send_value_surname(surname)
        self.WebTables.send_value_email(email)
        self.WebTables.send_value_age(age)
        self.WebTables.send_value_salary(salary)
        self.WebTables.send_value_department(department)
        self.WebTables.click_button_submit()
        self.WebTables.is_send_value_name(name)
        self.WebTables.is_send_value_surname(surname)
        self.WebTables.is_send_value_email(email)
        self.WebTables.is_send_value_age(age)
        self.WebTables.is_send_value_salary(salary)
        self.WebTables.is_send_value_department(department)
        self.WebTables.is_click_button_submit


@pytest.mark.parametrize("name, surname, email, age, salary, department", Data.get_test_data())
@pytest.mark.usefixtures("setup")
def test_no(name, surname, email, age, salary, department):
    DemoQa = PageDemoQa()
    DemoQa.get_page()
    assert DemoQa.is_open() == True, 'page is not opened'
    DemoQa.click_button_elements()
    Web = WebTables()
    Web.click_button_web_tables()
    Web.is_page_web_tables_open()
    Web.click_button_add()
    Web.send_value_name(name)
    Web.send_value_surname(surname)
    Web.send_value_email(email)
    Web.send_value_age(age)
    Web.send_value_salary(salary)
    Web.send_value_department(department)
    Web.click_button_submit()
    Web.is_send_value_name(name)
    Web.is_send_value_surname(surname)
    Web.is_send_value_email(email)
    Web.is_send_value_age(age)
    Web.is_send_value_salary(salary)
    Web.is_send_value_department(department)
    Web.is_click_button_submit


@pytest.mark.usefixtures("setup")
class Test1():

    def test_open_page(self):
        self.PageDemoQa = PageDemoQa()
        self.PageDemoQa.get_page()
        assert self.PageDemoQa.is_open() == all(
            [True for i in Data.data_access(f"{chr(92)}TestData.json", "DDT", "is_open", 1) if
             i == str("True")]), 'page is not opened'
        self.PageDemoQa.click_button_alerts_frame_windows()
        self.PageAlerts = PageAlerts()
        self.PageAlerts.click_button_alerts()
        assert self.PageAlerts.is_alerts_clicked() == Data.data_access(f"{chr(92)}TestData.json", "DDT",
                                                                       "is_alerts_clicked",
                                                                       1), 'Button alert was no clicked'
        self.PageAlerts.click_Button_To_See_Alert()
        assert self.PageAlerts.is_alert_open() == Data.data_access(f"{chr(92)}TestData.json", "DDT", "is_alert_open",
                                                                   1), 'Aler is not displayed'
        self.PageAlerts.accept_allert()
        try:
            assert self.PageAlerts.is_alert_open() != 'You clicked a button'
        except:
            pass
        self.PageAlerts.click_confirm_box()
        assert self.PageAlerts.is_alert_open_confirm_box() == Data.data_access(f"{chr(92)}TestData.json", "DDT",
                                                                               "is_alert_open_confirm_box",
                                                                               1), 'Aler is not displayed'
        self.PageAlerts.accept_allert()
        assert self.PageAlerts.is_dislayed_you_selected_ok() == Data.data_access(f"{chr(92)}TestData.json", "DDT",
                                                                                 "is_dislayed_you_selected_ok",
                                                                                 1), 'Alert was not accepted'
        self.PageAlerts.click_prompt_box()
        self.name = random_name()
        self.PageAlerts.send_input_prompt_box(self.name)
        assert self.PageAlerts.is_alert_open_please_enter_your_name() == Data.data_access(f"{chr(92)}TestData.json",
                                                                                          "DDT",
                                                                                          "is_alert_open_please_enter_your_name",
                                                                                          1), 'Alet window not opened'
        self.PageAlerts.accept_allert()
        assert self.PageAlerts.is_name_correct() == f'You entered {self.name}', 'Name is not true'


@pytest.mark.usefixtures("setup")
class Test2():

    def test_open_page(self):
        self.PageDemoQa = PageDemoQa()
        self.PageDemoQa.get_page()
        assert self.PageDemoQa.is_open() == True, 'page is not opened'
        self.PageDemoQa.click_button_alerts_frame_windows()
        self.NestedFrames = NestedFrames()
        self.Frame = Frame()
        self.NestedFrames.click_button_nested_frames()
        assert self.NestedFrames.is_nested_frames_opened() == True, "Page nested frames not opened"
        self.Frame.page_refres()
        self.Frame.switch_defoult()
        self.Frame.switch_frames_top()
        assert self.NestedFrames.is_page_nested_frames_changed_parent() == 'Parent frame', 'Frame not changed'
        self.Frame.page_refres()
        self.Frame.switch_defoult()
        self.Frame.switch_frames_top()
        self.Frame.swtich_frames_child()
        assert self.NestedFrames.is_page_nested_frames_changed_child() == 'Child Iframe', 'Frame not changed'
        self.Frame.switch_defoult()
        self.Frame.click_button_frames()
        assert self.Frame.is_frames_opened() == True, 'Page with Frames form is not open.'
        assert self.Frame.is_frame_correct() == True, 'Message from upper frame is not equal to the message from lower frame'


@pytest.mark.usefixtures("setup")
class Test4():

    def test_open_page(self):
        self.PageDemoQa = PageDemoQa()
        self.PageDemoQa.get_page()
        assert self.PageDemoQa.is_open() == True, 'page is not opened'
        self.PageDemoQa.click_button_alerts_frame_windows()
        self.BrowserWindows = BrowserWindows()
        self.BrowserWindows.click_browser_windows()
        assert self.BrowserWindows.is_button_new_tab() == True, ' Page not opened browser-windows'
        self.BrowserWindows.click_new_tab()
        name = self.BrowserWindows.save_tab_name()
        self.BrowserWindows.switch_tab_new(name)
        assert self.BrowserWindows.is_open_new_tab() == True, 'The new tab is not opened'
        self.BrowserWindows.close_tab()
        self.BrowserWindows.switch_tab_oryginal(name)
        assert self.BrowserWindows.is_button_new_tab() == True, ' Page not opened browser-windows'
        self.BrowserWindows.click_elements()
        self.PageLinks = PageLinks()
        assert self.PageLinks.is_page_links_open() == True, 'Page links not opened'
        name = self.BrowserWindows.save_tab_name()
        self.PageLinks.click_button_home()
        self.BrowserWindows.switch_tab_new(name)
        assert self.PageDemoQa.is_open() == True, 'page is not opened'
        self.BrowserWindows.switch_tab_oryginal(name)
        assert self.PageLinks.is_page_links_open() == True, 'Page links not opened'


@pytest.mark.usefixtures("setup")
class Test7(softest.TestCase):

    def test_no_7(self):
        self.PageDemoQa = PageDemoQa()
        self.PageDemoQa.get_page()
        assert self.PageDemoQa.is_open() == True, 'page is not opened'
        self.PageDemoQa.click_button_elements()
        self.PageUploadDownload = PageUploadDownload()
        self.PageUploadDownload.click_button_upload()
        assert self.PageUploadDownload.is_open_page_upload() == True, 'page is not open'
        self.PageUploadDownload.click_button_download()
        assert self.PageUploadDownload.is_file_exists() == True, 'File does not exist'
        self.PageUploadDownload.click_button_choose_file()
        assert self.PageUploadDownload.is_uploded() == True, 'The file was uploaded successfully'
