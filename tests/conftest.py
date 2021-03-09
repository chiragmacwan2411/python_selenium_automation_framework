from basePackage.pageFactory import *
import pytest


@pytest.fixture(scope="class")
def setUp(request, browser):
    # # application url
    # baseUrl = "http://www.demo.guru99.com/V4/index.php"
    #
    # # browser configuration
    # driver = webdriver.Chrome(executable_path="/Users/chiragkumarmacwan/Downloads/browserDrivers/chromedriver")
    # # driver = webdriver.Firefox(executable_path="/Users/chiragkumarmacwan/Downloads/browserDrivers/geckodriver")
    # driver.maximize_window()
    # driver.implicitly_wait(5)
    # driver.set_page_load_timeout(10)
    # driver.get(baseUrl)
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver

    # tear down
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")