from selenium.webdriver.common.by import By


class LocatorsMain:
    # HOW_MUCH_Q = (By.ID, "accordion__heading-0") # ссылка на Вопрос: Сколько это стоит
    # HOW_MUCH_A = (By.XPATH, "//*[@id='accordion__panel-0']/p") # ссылка на Ответ на вопрос "Сколько стоит"
    # WANT_MANI_SCOOTER_Q = (By.ID, "accordion__heading-1") # ссылка на Вопрос: Хочу несколько самокатов
    # WANT_MANI_SCOOTER_A = (By.XPATH, "//*[@id='accordion__panel-1']/p") # ссылка на Ответ на вопрос "Хочу несколько самокатов"
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//button[contains(@class,'Button_Middle__1CSJM')]") # Кнопка заказать в центре стриницы

