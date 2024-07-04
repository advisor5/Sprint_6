import pytest
import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from page_object.main_page import MainPage
from constants import Answers


class TestList:
    @allure.title('Тест ответов на вопросы')
    @allure.description(
    'Проверяем: когда нажимаешь на стрелочку, открывается корректный текст ответа на вопрос')
    @pytest.mark.parametrize(
    'number_question,number_answer',
    [
        ['0', Answers.HOW_MUCH],
        ['1', Answers.WANT_MANI_SCOOTER],
        ['2', Answers.HOW_CHECK_TIME_RENT],
        ['3', Answers.CAN_BE_ORDERED_TODAY],
        ['4', Answers.EXTEND_THE_ORDER],
        ['5', Answers.BRING_CHARGERS],
        ['6', Answers.CANCEL_THE_ORDER],
        ['7', Answers.LIVE_OUTSIDE_THE_MOSCOW_RING]
    ]
    )
    def test_questions_and_answers(self, number_question, number_answer, driver: WebDriver):
        main = MainPage(driver)
        main.scroll_to_questions()
        main.click_questions(number_question)
        
        actually_value = main.get_answer_text(number_question)
        expected_value = number_answer
        assert actually_value == expected_value
