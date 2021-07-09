import time
import math

import pytest


LINKS = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.fixture(scope="function")
def answer():
    correct_answer = math.log(int(time.time()))
    return correct_answer


@pytest.mark.parametrize("link", LINKS)
def test_pages(browser, answer, link):
    browser.get(link)
    area = browser.find_element_by_css_selector(".string-quiz__textarea")
    area.send_keys(str(answer))
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    text = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert text == "Correct!"
