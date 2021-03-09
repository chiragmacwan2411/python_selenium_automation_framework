import logging
import utilities.custom_logger as cl
from basePackage.selenium_driver import SeleniumDriver

class TestCaseStatus(SeleniumDriver):
    log = cl.Logger(logging.DEBUG)

    def __init__(self, driver):
        super(TestCaseStatus, self).__init__(driver)
        self.resultList = []

    def setRsult(self, result, resultMsg):
        try:
            if result is not None:
                if result:
                    self.resultList.append("-->PASS<--")
                    self.log.info("*** VERIFICATION SUCCESSFUL ***" + resultMsg)
                else:
                    self.resultList.append("|||||FAIL|||||")
                    self.log.error("*** VERIFICATION FAILED ***" + resultMsg)
                    self.take_screen_shot(resultMsg)
            else:
                self.resultList.append("|||||FAIL|||||")
                self.log.error("*** VERIFICATION FAILED ***" + resultMsg)
                self.take_screen_shot(resultMsg)
        except:
            self.resultList.append("|||||FAIL|||||")
            self.log.error("*** EXCEPTION OCCURRED ***" + resultMsg)
            self.take_screen_shot(resultMsg)

    # in case of multiple assertions, this is the non-final assertion
    def mark(self, result, resultMsg):
        self.setRsult(result, resultMsg)

    # this is the final assertion
    def mark_final(self, testCaseName, result, resultMsg):
        self.log.info("Starting execution of TC :: " +testCaseName)
        self.setRsult(result, resultMsg)
        if "FAIL" in self.resultList:
            self.log.error(testCaseName + "|||||TEST FAILED|||||" + "\n")
            self.resultList.clear()
            assert True == False
        else:
            self.log.error(testCaseName + "--->TEST PASSED<---" + "\n")
            self.resultList.clear()
            assert True == True