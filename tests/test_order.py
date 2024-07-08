import pytest
import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from page_object.base_page import BasePage
from page_object.main_page import MainPage
from page_object.order_page import OrderPage
from constants import Url
from constants import Title


class TestList:
    @allure.title('Тест кнопки "Заказать" вверху страницы')
    @allure.description(
    'Проверяем наличие заголовка "Для кого самокат" на странице формирования заказа')
    def test_order_button_header(self, base_page: BasePage, order_page: OrderPage):
        base_page.click_on_the_order_button_header()
        order_page.wait_order_form()
        
        actually_value = order_page.get_text_title_order_form()
        expected_value = Title.SCOOTER_FOR
        assert actually_value == expected_value
    
    @allure.title('Тест кнопки "Заказать" внизу страницы')
    @allure.description(
    'Проверяем наличие заголовка "Для кого самокат" на странице формирования заказа')
    def test_order_button_down(self, base_page: BasePage, main_page: MainPage, order_page: OrderPage):
        base_page.wait_cookie_botton()
        base_page.click_cookie_botton()
        main_page.scroll_to_down_botton()
        main_page.click_on_the_order_button_middle()
        
        actually_value = order_page.get_text_title_order_form()
        expected_value = Title.SCOOTER_FOR
        assert actually_value == expected_value

    @allure.title('Тест перехода на главную страницу, если нажать на логотип "Самоката"')
    @allure.description(
    'Проверяем текущий URL с URL сервиса "Яндекс.Самокат"')
    def test_click_on_scooter_button_transfer_to_home(self, base_page: BasePage, order_page: OrderPage, driver: WebDriver):
        base_page.click_on_the_order_button_header()
        order_page.wait_order_form()
        base_page.click_on_the_scooter_button()
        
        actually_value = driver.current_url
        expected_value = Url.HOST    
        assert actually_value == expected_value
    
    @allure.title('Тест перехода на главную Дзена, если нажать на логотип "Яндекс"')
    @allure.description(
    'Проверяем текущий URL с URL главной страницей Дзена')
    def test_click_on_yandex_button_transfer_to_dzen(self, base_page: BasePage, order_page: OrderPage, driver: WebDriver):
        base_page.click_on_the_order_button_header()
        order_page.wait_order_form()
        window_before = driver.window_handles[0]
        base_page.click_on_the_yandex_button()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        base_page.wait_dzen_site()

        actually_value = driver.current_url
        expected_value = Url.DZEN_SITE
        assert actually_value == expected_value

    @allure.title('Тест заполнения формы заказа')
    @allure.description(
    'Проверяем что появилось всплывающее окно с сообщением "Заказ оформлен" при успешном создании заказа.')
    @pytest.mark.parametrize(
    'name,surname,address,station,telefon,data,days,color',
    [
        ['Сергей', 'Иванов', 'Москва, ул. Ленина 5, кв. 6', 'Комсомольская', '+79098327080', '10', 'сутки', 'black'],
        ['Игорь', 'Петров', 'Санкт-Петербург, ул. Ленина 5, кв. 6', 'Сокольники', '+79098327081', '15', 'четверо суток', 'grey']]
    )
    def test_order(self, name, surname, address, station, telefon, data, days, color, order_page: OrderPage):                
        order_page.ordering_scooter(name, surname, address, station, telefon, data, days, color)
    
        actually_value = order_page.get_succeed_order()
        expected_value = Title.ORDER_REGISTRERED
        assert expected_value in actually_value
