import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class PageLocators:
    """Class for describing element locators"""

    PREVIOUS_LINK = "http://suninjuly.github.io/registration1.html"
    LINK = "http://suninjuly.github.io/registration2.html"
    FIRST_NAME = ".first_block .form-group.first_class .form-control.first"
    LAST_NAME = ".first_block .form-group.second_class .form-control.second"
    EMAIL = ".first_block .form-group.third_class .form-control.third"
    PHONE = ".second_block .form-group.first_class .form-control.first"
    ADRESS = ".second_block .form-group.second_class .form-control.second"
    BUTTON = ".btn.btn-default"


class Page:
    """Basic page class, using it both for first and second pages"""

    def __init__(self, browser):
        self.browser = browser

    def open_site(self, link):
        self.browser.get(link)

    def fill_all_fields(self):
        self.browser.find_element(By.CSS_SELECTOR, PageLocators.FIRST_NAME).send_keys(
            "Ivan"
        )
        self.browser.find_element(By.CSS_SELECTOR, PageLocators.LAST_NAME).send_keys(
            "Ivanov"
        )
        self.browser.find_element(By.CSS_SELECTOR, PageLocators.EMAIL).send_keys(
            "Ivan@tut.by"
        )
        self.browser.find_element(By.CSS_SELECTOR, PageLocators.PHONE).send_keys(
            "12345678"
        )
        self.browser.find_element(By.CSS_SELECTOR, PageLocators.ADRESS).send_keys(
            "Ivanovo"
        )

    def send_the_data(self):
        self.browser.find_element(By.CSS_SELECTOR, PageLocators.BUTTON).click()


class TestPage(unittest.TestCase):
    """
    Testing our two pages.
    First page must pass, second page must raise NoSuchElementExeption
    """

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.page = Page(self.browser)

    def tearDown(self):
        self.browser.quit()

    def test_first_page_passes(self):
        """Assert our first page allows user to register"""

        self.page.open_site(PageLocators.PREVIOUS_LINK)
        self.page.fill_all_fields()
        self.page.send_the_data()

    def test_second_page_exeption_raises(self):
        """Assert our second page misses one field and Exeption is raises"""

        with self.assertRaises(NoSuchElementException):
            self.page.open_site(PageLocators.LINK)
            self.page.fill_all_fields()
            self.page.send_the_data()


if __name__ == "__main__":
    unittest.main()
