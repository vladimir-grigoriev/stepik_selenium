import time
from selenium.webdriver.remote.webelement import WebElement

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(LINK)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert isinstance(button, WebElement), "Button not found"
    time.sleep(5)