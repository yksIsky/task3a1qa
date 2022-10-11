from Form.PageDomoQa import PageDemoQa
import pytest
from Form.BrowserWindows import BrowserWindows
from Form.PageLinks import PageLinks


@pytest.mark.usefixtures("setup")
class Test4():

    def test_1(self):
        self.test = PageDemoQa()
        self.test.get_page()
        assert self.test.is_open() == True, 'page is not opened'
        self.test.click_button_alerts_frame_windows()
        self.test1 = BrowserWindows()
        self.test1.click_browser_windows()
        assert self.test1.is_button_new_tab() == True, ' Page not opened browser-windows'
        name = self.test1.save_tab_name()
        self.test1.click_new_tab()
        self.test1.switch_tab_new(name)
        assert self.test1.is_open_new_tab() == True , 'The new tab is not opened'
        self.test1.close_tab()
        self.test1.switch_tab_oryginal(name)
        assert self.test1.is_button_new_tab() == True, ' Page not opened browser-windows'
        self.test1.click_elements()
        self.test2 = PageLinks()
        assert self.test2.is_page_links_open() == True, 'Page links not opened'
        name = self.test1.save_tab_name()
        self.test2.click_button_home()
        self.test1.switch_tab_new(name)
        assert self.test.is_open() == True, 'page is not opened'
        self.test1.switch_tab_oryginal(name)
        assert self.test2.is_page_links_open() == True, 'Page links not opened'
