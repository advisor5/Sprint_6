import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from locators.base_page_locators import LocatorsBase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Url


class BasePage:
    order_button_header = (LocatorsBase.ORDER_BUTTON_TOP)
    cookie_button = (LocatorsBase.COOKIE_BUTTON)
    scooter_botton = (LocatorsBase.SCOOTER_BUTTON)
    yandex_button = (LocatorsBase.YANDEX_BUTTON)

    def __init__(self,  driver: WebDriver):
        self.driver = driver

    @allure.step('Ожидаем появления уведомления об использовании куков')
    def wait_cookie_botton(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.cookie_button))
    
    @allure.step('Кликаем на кнопку "Да все привыкли"')
    def click_cookie_botton(self):
        self.driver.find_element(*self.cookie_button).click()
    
    @allure.step('Кликаем на кнопку "Заказать" вверху страницы')
    def click_on_the_order_button_header(self):
        self.driver.find_element(*self.order_button_header).click()

    @allure.step('Кликаем на лого "Самокат" вверху страницы')
    def click_on_the_scooter_button(self):
        self.driver.find_element(*self.scooter_botton).click()
    
    @allure.step('Кликаем на лого "Яндекс" вверху страницы')
    def click_on_the_yandex_button(self):
        self.driver.find_element(*self.yandex_button).click()
        
    @allure.step('Ожидаем загрузку главной страницы Дзена')
    def wait_dzen_site(self):
        WebDriverWait(self.driver, 5).until(EC.url_contains(Url.DZEN_SITE))
