import math
import time

from selenium import webdriver


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")

    my_string = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element_by_link_text(my_string)
    link.click()
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Minsk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Belarus")
    btn = browser.find_element_by_tag_name("button.btn.btn-default")
    btn.click()
    
    

finally:
    i = input(">>> Press Enter to escape ")
    browser.quit()