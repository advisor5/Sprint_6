import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from locators.main_page_locators import LocatorsMain
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class MainPage:
    order_button_middle = (LocatorsMain.ORDER_BUTTON_MIDDLE)

    def __init__(self,  driver: WebDriver):
        self.driver = driver
    
    @allure.step('Прокручиваем страницу до Вопросов')
    def scroll_to_questions(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    @allure.step('Кликаем на вопрос')
    def click_questions(self, number_question):
        question = (By.ID, f"accordion__heading-{number_question}")
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(question))       
        self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text(self, number_question):
        answer = (By.XPATH, f"//*[@id='accordion__panel-{number_question}']/p")
        return WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(answer)).text
    
    @allure.step('Прокручиваем страницу до кнопки "Заказать", внизу страницы')
    def scroll_to_down_botton(self):
        element = self.driver.find_element(*self.order_button_middle)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Кликаем на кнопку "Заказать" внизу страницы')
    def click_on_the_order_button_middle(self):
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(self.order_button_middle)).click()
