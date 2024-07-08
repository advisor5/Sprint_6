from selenium.webdriver.common.by import By


class LocatorsBase:
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()='Заказать']") # Кнопка Заказать в хедере
    SCOOTER_BUTTON = (By.XPATH, "//img[@src='/assets/scooter.svg']") # Логотип Самокат
    YANDEX_BUTTON = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]") # Логотип Яндекс
    COOKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']") # Окно с куки
