from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    treaseru = browser.find_element_by_id('treasure')

    treasere_value_x = treaseru.get_attribute('valuex')

    x = calc(treasere_value_x)
    print(x)

    field = browser.find_element_by_id('answer')
    field.send_keys(x)

    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    option1.click()

    # option2 = browser.find_element_by_css_selector("[type='radio']")
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
