import pytest
from utils.driver_factory import DriverFactory

class BaseTest:
    @pytest.fixture(scope="function", autouse=True) # This fixture will run before each test function
    def setup(self, request):
        self.playwright, self.browser, self.context, self.page= DriverFactory.get_browser()
        request.cls.page= self.page # Make the page available to the test class
        yield # This is where the test will run
        self.browser.close() # Close the browser after the test is done
        self.playwright.stop() # Stop Playwright after the test is done
