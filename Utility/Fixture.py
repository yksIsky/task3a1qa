from Utility.Driver import BrowserUtils
import pytest
from Utility.DataUtility import Data
import time


@pytest.fixture(scope="session")
def setup(request):
    driver = BrowserUtils.return_instance()

    yield driver
    driver.quit()
    BrowserUtils.clear()
