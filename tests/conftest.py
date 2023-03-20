from pytest import fixture
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service

from conf.paths import geckodriver


@fixture
def driver():
    options = FirefoxOptions()
    service = Service(executable_path=geckodriver)
    options.headless = True
    firefox = Firefox(options=options, service=service)
    firefox.maximize_window()
    yield firefox
    firefox.close()
    firefox.quit()
