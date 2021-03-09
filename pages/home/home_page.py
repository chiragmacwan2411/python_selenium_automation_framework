from basePackage.selenium_driver import SeleniumDriver
import utilities.custom_logger as lg

class Home_Page(SeleniumDriver):
    log = lg.Logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators of the Home Page
    _logOut_btn = "//a[contains(text(),'Log out')]" # xpath

    def logout(self):
        self.element_click(self._logOut_btn, "xpath")
        return self.verify_alert_popUp()
