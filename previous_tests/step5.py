from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")
for elem in browser.find_elements_by_tag_name("input"):
    elem.send_keys("my value")
browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]").click()
input()
browser.quit()
