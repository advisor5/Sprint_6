import pytest
from selenium import webdriver
from page_object.base_page import BasePage
from page_object.main_page import MainPage
from page_object.order_page import OrderPage

from constants import Url

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Url.HOST)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page

@pytest.fixture
def base_page(driver):
    base = BasePage(driver)
    return base

@pytest.fixture
def order_page(driver):
    order = OrderPage(driver)
    return  order
