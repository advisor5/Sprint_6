import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from locators.order_page_locators import LocatorsOrder
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class OrderPage(BasePage):
    title_order = (LocatorsOrder.ORDER_HEADER_TITLE)
    field_name = (LocatorsOrder.FIELD_NAME)
    field_surname = (LocatorsOrder.FIELD_SURNAME)
    field_address = (LocatorsOrder.FIELD_ADDRESS)
    field_station = (LocatorsOrder.FIELD_STATION)
    field_telefon = (LocatorsOrder.FIELD_TELEFON)
    next_button = (LocatorsOrder.NEXT_BOTTON)
    title_about_rent = (LocatorsOrder.TITLE_ABOUT_RENT)
    field_day_rent = (LocatorsOrder.FIELD_DAYS_RENT)
    data_delivery = (LocatorsOrder.FIELD_WHEN_DELIVERY)
    order_button = [*LocatorsOrder.ORDER_BOTTON]
    windows_want_order = [LocatorsOrder.WINDOWS_WANT_ORDER]
    yes_button = [*LocatorsOrder.YES_BUTTON]
    succeed_order = [LocatorsOrder.ORDER_IS_PROCESSED]

    def __init__(self,  driver: WebDriver):
        self.driver = driver

    @allure.step('Ожидаем видимость заголовка "Для кого самокат" на странице заказа')
    def wait_order_form(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.title_order))

    @allure.step('Получаем текст заголовка "Для кого самокат" на первой странице формирования заказа')
    def get_text_title_order_form(self):
        return self.driver.find_element(*self.title_order).text

    @allure.step('Заполняем поле "Имя"')
    def set_name(self, name):
        self.driver.find_element(*self.field_name).send_keys(name)
    
    @allure.step('Заполняем поле "Фамилия"')
    def set_surname(self, surname):
        self.driver.find_element(*self.field_surname).send_keys(surname)
    
    @allure.step('Заполняем поле "Адрес"')
    def set_address(self, address):
        self.driver.find_element(*self.field_address).send_keys(address)

    @allure.step('Нажимаем на поле "Станция метро"')
    def click_field_station(self):
        self.driver.find_element(*self.field_station).click()

    @allure.step('Выбираем странцию метро из списка')
    def choice_station_from_list(self, station):
        self.driver.find_element(By.XPATH, f"//div[text()='{station}']").click()

    @allure.step('Заполняем поле "Телефон"')
    def set_telefon(self, telefon):
        self.driver.find_element(*self.field_telefon).send_keys(telefon)

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()
    
    @allure.step('Ожидаем появлениея заголовка "Про аренду" на второй странице формирования заказа')
    def wait_two_page_order(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.title_about_rent))

    @allure.step('Нажимаем на поле "Когда привезти самокат"')
    def click_data_delivery(self):
        self.driver.find_element(*self.data_delivery).click()

    @allure.step('Выбираем в появившемся календаре дату')
    def choice_data_delivery(self, data):
        self.driver.find_element(By.XPATH, f"//div[contains(@aria-label,' {data}-е июля 2024 г.')]").click()
    
    @allure.step('Нажимаем на поле "Срок аренды"')
    def click_days_rent(self):
        self.driver.find_element(*self.field_day_rent).click()

    @allure.step('Выбираем из списка количество дней аренды')
    def choice_days_rent(self, days):
        self.driver.find_element(By.XPATH, f"//div[text()='{days}']").click()

    @allure.step('Выбираем чекбокс с цветом самоката')
    def choice_color_scooter(self, color):
        self.driver.find_element(By.ID, f"{color}").click()

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Ожидаем загрузку окно с подтверждением заказа')
    def wait_for_load_window(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(*self.windows_want_order))

    @allure.step('Нажамаем на кнопку "Да"')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Получаем текст залоговка "Заказ оформлен" при успешном создании заказа')
    def get_succeed_order(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(*self.succeed_order)).text

    def ordering_scooter(self, name, surname, address, station, telefon, data, days, color):
        self.wait_cookie_botton()
        self.click_cookie_botton()
        self.click_on_the_order_button_header()
        
        self.wait_order_form()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_field_station()
        self.choice_station_from_list(station)
        self.set_telefon(telefon)
        self.click_next_button()
        self.wait_two_page_order()
        self.click_data_delivery()
        self.choice_data_delivery(data)
        self.click_days_rent()
        self.choice_days_rent(days)
        self.choice_color_scooter(color)
        self.click_order_button()
        self.wait_for_load_window()
        self.click_yes_button()
