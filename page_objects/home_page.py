from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class HomePage(BasePage):
    __url = "https://www.typing.com/student/lessons"
    __account_dropdown = (By.XPATH, "//nav//*[@class='split-cell dropdown-trigger']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def account(self) -> str:
        return self._find(self.__account_dropdown).text

