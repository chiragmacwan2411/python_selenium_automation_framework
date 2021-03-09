from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.testStatus import TestCaseStatus
from basePackage.selenium_driver import SeleniumDriver

@pytest.mark.usefixtures("setUp")
class Login_Tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def login_Class_setUp(self, setUp):
        self.loginPage = LoginPage(self.driver)
        self.status = TestCaseStatus(self.driver)
        self.sel = SeleniumDriver(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        # test case 1 --> verify successful login
        result = False
        page_title = self.loginPage.verify_login("mngr308361", "zedaheq")

        if page_title == "Guru99 Bank Manager HomePage":
            result = True
        self.status.mark_final("test_valid_login", result,
                               "Valid_login verified :: if not first check if the expired credentials")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        # test case 2 --> verify invalid login
        result = False
        invalid_login_popup = self.loginPage.verify_invalid_login("invalid_username","invalid_password")

        if invalid_login_popup == "User or Password is not valid":
            result = True
        self.status.mark_final("test_invalid_login", result, "inValid_login prevented and verified")