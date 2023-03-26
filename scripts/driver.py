from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service

from conf.paths import geckodriver


class Driver:

    def __init__(self):
        self.driver = None
        self.opts = FirefoxOptions()
        self.service = Service(executable_path=geckodriver)
        self.opts.add_argument("-headless")

    def __enter__(self):
        self.driver = Firefox(options=self.opts, service=self.service)
        self.driver.maximize_window()
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self.driver.quit()
