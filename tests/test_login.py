import pytest
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage


class TestLoginPositive:

    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.positive
    def test_login(self, driver):
        username_value = "TestUser1221"
        password_value = "TestPassword1221!"

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username_value, password_value)

        home_page = HomePage(driver)
        home_page.wait_until_url_changed()
        assert home_page.current_url == home_page.expected_url, f"page {home_page.expected_url} was not opened"
        assert home_page.account == username_value.lower(), f"account '{username_value.lower()}' was not displayed"
