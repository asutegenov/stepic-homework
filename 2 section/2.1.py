from selenium import webdriver
import time, math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    field = browser.find_element_by_id('answer')
    field.send_keys(y)

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