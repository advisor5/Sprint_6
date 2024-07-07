from selenium.webdriver.common.by import By


class LocatorsOrder:
    # Страница 1 заказа
    ORDER_HEADER_TITLE = (By.XPATH, "//div[contains(@class,'Order_Header')]") # Заголовок на странице зказа
    FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']") #  Поле Имя
    FIELD_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']") #  Поле Фамилия
    FIELD_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") #  Поле Адрес
    FIELD_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']") #  Поле Станция метро
    FIELD_TELEFON = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") #  Поле телефон
    NEXT_BOTTON = (By.XPATH, "//button[text()='Далее']") #  Кнопка Далее

    # Страница 2 заказа 
    TITLE_ABOUT_RENT = (By.XPATH, "//div[text()='Про аренду']") # Залоговок Про аренду
    FIELD_WHEN_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # Выбор даты доставки
    FIELD_DAYS_RENT = (By.XPATH, "//div[contains(@class,'Dropdown-root')]") # Поле для выбора дней аренды
    ORDER_BOTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']") #  Кнопка Заказать
    WINDOWS_WANT_ORDER = (By.XPATH, "//div[text()='Хотите оформить заказ?']") # Окно - Хотите оформить заказ
    YES_BUTTON = (By.XPATH, "//button[text()='Да']") # Кнопка ДА
    ORDER_IS_PROCESSED = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]") # Заказ оформлен
