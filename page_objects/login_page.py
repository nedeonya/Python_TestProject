from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://www.typing.com/student/login"
    __username_input = (By.ID, "form-ele-username")
    __password_input = (By.ID, "form-ele-password")
    __next_button = (By.XPATH, "//button[@type='submit']")
    __error_message = (By.XPATH, "//*[@class='is-error']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def login(self, username, password):
        super()._send_keys(self.__username_input, username)
        super()._click(self.__next_button)
        super()._send_keys(self.__password_input, password)
        super()._click(self.__next_button)

    def login_only_username(self, username):
        super()._send_keys(self.__username_input, username)
        super()._click(self.__next_button)

    def verify_error_message_text(self, error_text) -> bool:
        self.wait_until_text_present(self.__error_message, error_text)
        return super()._get_text(self.__error_message) == error_text
