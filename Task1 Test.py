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



@pytest.mark.usefixtures("setup")
class Test2():

    def test_open_page(self):
        self.PageDemoQa = PageDemoQa()
        self.PageDemoQa.get_page()
        assert self.PageDemoQa.is_open() == True, 'page is not opened'