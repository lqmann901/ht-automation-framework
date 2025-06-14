import pytest
from utils.driver_factory import create_driver

@pytest.fixture

def browser():
    driver = create_driver()
    driver.get("https://www.google.com")
    yield driver
    driver.quit()