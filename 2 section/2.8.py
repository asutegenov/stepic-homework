from selenium import webdriver
import time, math, pyperclip

def calc(x):
    x = int(x)
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    button1 = browser.find_element_by_class_name('trollface')
    button1.click()

    second_page = browser.window_handles[1]
    browser.switch_to.window(second_page)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    y = str(y)

    field = browser.find_element_by_id('answer')
    field.send_keys(y)

    button2 = browser.find_element_by_class_name('btn')
    button2.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToCopyBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToCopyBoard)
    alert.accept()

finally:
    time.sleep(1)
    browser.quit()