from Form.PageDomoQa import PageDemoQa
import pytest
from Utility.DataUtility import Data
from Form.PageAlerts import PageAlerts

@pytest.mark.usefixtures("setup")
class Test1():

    def test_open_page(self):
        self.test = PageDemoQa()
        self.test.get_page()
        assert self.test.is_open() == True, 'page is not opened'
        self.test.click_button_alerts_frame_windows()
        self.test = PageAlerts()
        self.test.click_button_alerts()
        assert self.test.is_alerts_clicked() == True, 'Button alert was no clicked'
        self.test.click_Button_To_See_Alert()
        assert self.test.is_alert_open() == 'You clicked a button', 'Aler is not displayed'
        self.test.accept_allert()
        try:
            assert self.test.is_alert_open() != 'You clicked a button'
        except:
            pass
        self.test.click_confirm_box()

        assert self.test.is_alert_open_confirm_box() == 'Do you confirm action?', 'Aler is not displayed'
        self.test.accept_allert()
        assert self.test.is_dislayed_you_selected_ok() == True, 'Alert was not accepted'

        self.test.click_prompt_box()
        self.test.send_input_prompt_box()
        assert self.test.is_alert_open_please_enter_your_name() == 'Please enter your name', 'Alet window not opened'
        self.test.accept_allert()
        x = Data.data_access("\TestData.json", "Person", "Name", 1)
        assert self.test.is_name_correct() == f'You entered {x}', 'Not true'


