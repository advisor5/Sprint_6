from selenium.webdriver.common.by import By


class LocatorsBase:
    ORDER_BUTTON_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']") # Кнопка Заказать в хедере
    SCOOTER_BUTTON = (By.XPATH, "//img[@src='/assets/scooter.svg']") # Логотип Самокат
    YANDEX_BUTTON = (By.CLASS_NAME, "Header_LogoYandex__3TSOI") # Логотип Яндекс
    COOKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']") # Окно с куки

