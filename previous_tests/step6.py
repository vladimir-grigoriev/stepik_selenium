from os import link
import time

from selenium import webdriver

links = {
    "1": "http://suninjuly.github.io/registration1.html",
    "2": "http://suninjuly.github.io/registration2.html",
}

try:
    browser = webdriver.Chrome()
    link = links["2"]
    browser.get(link)
    browser.find_element_by_css_selector(
        ".first_block input.form-control.first"
    ).send_keys("Ivan")
    browser.find_element_by_css_selector(
        ".first_block input.form-control.second"
    ).send_keys("Ivanov")
    browser.find_element_by_css_selector(
        ".first_block input.form-control.third"
    ).send_keys("Ivan@mail.ru")

    browser.find_element_by_class_name("btn.btn-default").click()

    welcome_text_elt = browser.find_element_by_css_selector("h1")
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!!"

finally:
    time.sleep(5)
    browser.quit()
