import datetime
from os.path import join

from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service

from conf.paths import geckodriver_dir, screenshots_dir


class Driver:

    def __init__(self):
        self.driver = None
        self.opts = FirefoxOptions()
        self.service = Service(executable_path=geckodriver_dir)
        self.opts.add_argument("-headless")

    def __enter__(self):
        self.driver = Firefox(options=self.opts, service=self.service)
        self.driver.maximize_window()
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            filename = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S.png")
            filepath = join(screenshots_dir, filename)
            self.driver.save_screenshot(filepath)
        self.driver.close()
        self.driver.quit()
