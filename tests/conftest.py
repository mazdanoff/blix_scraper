from pytest import fixture
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions

from conf.paths import geckodriver


@fixture
def driver():
    options = FirefoxOptions()
    options.headless = True
    firefox = Firefox(options=options, executable_path=geckodriver)
    firefox.maximize_window()
    yield firefox
    firefox.close()
    firefox.quit()
