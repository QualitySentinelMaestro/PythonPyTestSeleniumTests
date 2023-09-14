import pytest

from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage


class Test_Login(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.BASE_URL)
        assert title == TestData.BASE_URL

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)



