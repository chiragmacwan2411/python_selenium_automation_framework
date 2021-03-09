import os
import time
from traceback import print_stack
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as lg


class SeleniumDriver():
    log = lg.Logger()

    def __init__(self, driver):
        self.driver = driver

    def take_screen_shot(self, resultMsg):
        fileName = resultMsg + "." + str(round(time.time()*1000)) + ".png"
        screenShotDir = "../screenshots/"
        relativeFileName = screenShotDir + fileName
        currentDir = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDir, relativeFileName)
        destinationDir = os.path.join(currentDir, screenShotDir)

        try:
            if not os.path.exists(destinationDir):
                os.makedirs(destinationDir)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to dir " + destinationFile)
        except:
            self.log.info("Exception occurred")
            print_stack()
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("locator type " + locatorType + " is not supported/valid")

    def getElement(self, locator, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            self.log.info("element not found with locator : "+locator+ " locator type: " + locatorType)
        return element

    def isElementPresent(self, locator, locatorType):
        try:
            element = self.getElement(locator,locatorType)
            if element is not None:
                return True
            else:
                self.log.info("Element not present : " + " locator " + locator + " Locator type " + locatorType)
        except:
            self.log.info("Element not found")
            print_stack()

    def element_click(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element : locator= " + locator + " : locatortype= " + locatorType)
        except:
            self.log.info("Cannot click on element : locator= " + locator + " : locatortype= " + locatorType)
            print_stack()

    def send_keys_to_element(self, key, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(key)
            self.log.info("Sent Key on element : locator= " + locator + " : locatortype=" + locatorType)
        except:
            self.log.info("Cannot Send Key on element : locator= " + locator + " : locatortype= " + locatorType)

            print_stack()

    def wait_for_element(self, locator, locatorType, timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum " + str(timeout) + " seconds for the element to be clickable.")
            wait = WebDriverWait(self.driver, 10, poll_frequency=pollFrequency, ignored_exceptions=[NoSuchElementException,
                                                                      ElementNotSelectableException,
                                                                      ElementNotVisibleException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            # print("Element found")
        except:
            self.log.info("Element not found with locator " + locator+" locator type " + locatorType)
            print_stack()
        return element

    def verify_alert_popUp(self):
        alert_msg = None
        try:
            # wait = WebDriverWait(self.driver,3).until(EC.alert_is_present(),"TimedOut")
            time.sleep(.2)
            _alert = self.driver.switch_to.alert
            alert_msg = _alert.text
            _alert.accept()
        except:
            self.log.info("No Alert Found !")
        return alert_msg