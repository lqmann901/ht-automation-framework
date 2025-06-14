import pytest
from pages.login_page import LoginPage
from utils.base_test import BaseTest
@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):
    def test_valid_login(self):
        login_page = LoginPage (self.page)
        login_page.load()
        login_page.login("admin","admin123")
        assert self.page.url == "https://example.com/dashboard", "Login failed or redirected to wrong page"    