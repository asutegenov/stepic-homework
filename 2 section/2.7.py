from selenium import webdriver
import time, math
import pyperclip


def calc(x):
    x = int(x)
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    button_one_page = browser.find_element_by_tag_name('button')
    button_one_page.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element= browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    y = str(y)

    field = browser.find_element_by_id('answer')
    field.send_keys(y)

    button = browser.find_element_by_class_name('btn')
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    alert.accept()


finally:
    time.sleep(0)
    browser.quit()
