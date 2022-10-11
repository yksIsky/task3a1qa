from Form.PageDomoQa import PageDemoQa
import softest
import pytest
from Form.PageUploadDownload import PageUploadDownload
from Utility.Fixture import setup


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
