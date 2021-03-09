from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        # application url
        baseUrl = "http://www.demo.guru99.com/V4/index.php"

        # browser configuration
        if self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="/Users/chiragkumarmacwan/Downloads/browserDrivers/geckodriver")
        else:
            driver = webdriver.Chrome(executable_path="/Users/chiragkumarmacwan/Downloads/browserDrivers/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(10)
        driver.get(baseUrl)
        return driver