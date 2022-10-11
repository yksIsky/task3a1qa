from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from pathlib import Path
import os


class BrowserFacory():

    @staticmethod
    def BrwoserFactory(browser):
        filepath_real = Path(os.path.dirname(os.path.realpath(__file__)))
        script_dir = str(filepath_real.parent)
        if browser == "Chrome":

            BrowserMode = webdriver.ChromeOptions()
            BrowserMode.add_argument("--incognito")
            prefs = {"download.default_directory":f"{script_dir}"}
            BrowserMode.add_experimental_option("prefs",prefs)



            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=BrowserMode)
            driver.maximize_window()
            return driver

        elif browser == "Firefox":

            options=Options()
            options.set_preference("browser.privatebrowsing.autostart", True)
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.manager.showWhenStarting", False)
            options.set_preference("browser.download.dir", f"{script_dir}")
            options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(options=options,service=service)
            return driver
        elif browser == "IDE":
            pass
        else:
            'Unsupported browser'