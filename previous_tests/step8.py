import math

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("treasure").get_attribute("valuex")
    result = calc(x)
    browser.find_element_by_id("answer").send_keys(result)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button").click()
finally:
    input()
    browser.quit()