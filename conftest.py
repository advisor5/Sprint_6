import pytest
from selenium import webdriver
from constants import Url

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Url.HOST)
    yield driver
    driver.quit()