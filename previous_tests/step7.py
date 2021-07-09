import math

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element_by_id("input_value").text)
    result = calc(x)
    browser.find_element_by_id("answer").send_keys(result)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button").click()


finally:
    input()
    browser.quit()