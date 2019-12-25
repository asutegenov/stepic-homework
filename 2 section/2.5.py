from selenium import webdriver
import time
import math

def calc(x):
    x = int(x)
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    y = str(y)
    
    field = browser.find_element_by_id('answer')
    field.send_keys(y)

    button = browser.find_element_by_tag_name('button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    option2 = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(20)
    browser.quit()


