import pytest
from page_objects.login_page import LoginPage


class TestLoginNegative:

    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, error_text",
                             [("IncorrectTestUser", "TestPassword1221!",
                               'No account with username "IncorrectTestUser" was found')])
    def test_login_negative_username(self, driver, username, password, error_text):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login_only_username(username)
        assert login_page.verify_error_message_text(error_text), f"error message {error_text} was not displayed"

    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, error_text",
                             [("TestUser1221", "IncorrectPassword", "Incorrect password")])
    def test_login_negative_password(self, driver, username, password, error_text):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)
        assert login_page.verify_error_message_text(error_text), f"error message {error_text} was not displayed"
