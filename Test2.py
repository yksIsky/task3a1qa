from Form.PageDomoQa import PageDemoQa
import pytest
from Form.PageNestedFrames import NestedFrames
from Form.PageFrames import Frame

@pytest.mark.usefixtures("setup")
class Test2():

    def test_open_page(self):
        self.test = PageDemoQa()
        self.test.get_page()
        assert self.test.is_open() == True, 'page is not opened'
        self.test.click_button_alerts_frame_windows()
        self.test.clic_button_nested_frames()
        self.test = Frame()
        self.test1 = NestedFrames()
        assert self.test1.is_nested_frames_opened() == True, "Page nested frames not opened"
        self.test.page_refres()
        self.test.switch_defoult()
        self.test.switch_frames_top()
        assert self.test1.is_page_nested_frames_changed_parent() == 'Parent frame', 'Frame not changed'
        self.test.page_refres()
        self.test.switch_defoult()
        self.test.switch_frames_top()
        self.test.swtich_frames_child()
        assert self.test1.is_page_nested_frames_changed_child() == 'Child Iframe', 'Frame not changed'
        self.test.switch_defoult()
        self.test.click_button_frames()
        assert self.test.is_frames_opened()  == True,  'Page with Frames form is not open.'
        assert self.test.is_frame_correct() == True,  'Message from upper frame is not equal to the message from lower frame'