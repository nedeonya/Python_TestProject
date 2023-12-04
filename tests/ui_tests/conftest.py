import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
# @pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    if browser == "chrome":
        _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        _driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected browsers are 'chrome' or 'firefox', but was '{browser}'")
    print(f"init {browser} driver...")
    yield _driver
    print(f"...quit {browser} driver")
    _driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="set up browser: chrome or firefox"
    )
