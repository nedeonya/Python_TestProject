from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    __timeout = 10

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _send_keys(self, locator: tuple, text, timeout: int = __timeout):
        self.wait_until_visible(locator, timeout)
        self._find(locator).send_keys(text)

    def _get_text(self, locator: tuple, timeout: int = __timeout):
        self.wait_until_visible(locator, timeout)
        return self._find(locator).text

    def _click(self, locator: tuple, timeout: int = __timeout):
        self.wait_until_visible(locator, timeout)
        self._find(locator).click()

    def wait_until_visible(self, locator: tuple, timeout: int = __timeout):
        Wait(self._driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_text_present(self, locator: tuple, text, timeout: int = __timeout):
        Wait(self._driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def wait_until_url_changed(self, timeout: int = __timeout):
        Wait(self._driver, timeout).until(EC.url_changes(self.current_url))

    @property
    def current_url(self) -> str:
        return self._driver.current_url
