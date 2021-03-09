from basePackage.selenium_driver import SeleniumDriver
import utilities.custom_logger as lg

class LoginPage(SeleniumDriver):
    log = lg.Logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators of home page
    _username_inputBx = "uid"
    _password_inputBx = "password"
    _login_btn = "btnLogin"


    # methods to perform actions on element
    def enter_username(self, username):
        self.send_keys_to_element(username, self._username_inputBx, "name")

    def enter_password(self, password):
        self.send_keys_to_element(password, self._password_inputBx, "name")

    def click_login_btn(self):
        self.element_click(self._login_btn, "name")


    # login test method
    def verify_login(self, username, password):
        # enter username into username field
        self.enter_username(username)

        # enter password into password field
        self.enter_password(password)

        # after entering username and password, click login button
        self.click_login_btn()

        # return  self.driver.title

    def verify_succssful_login(self, username, password):
        self.verify_login(username, password)
        return self.driver.title

    def verify_invalid_login(self, username, password):
        self.verify_login(username, password)
        return self.verify_alert_popUp()