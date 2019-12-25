from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math

def sum (a,b):
    a = int(a)
    b = int(b)
    return a + b

try:
    browser = webdriver.Chrome()
    # browser.get('http://suninjuly.github.io/selects1.html')
    browser.get('http://suninjuly.github.io/selects2.html')

    num1_element = browser.find_element_by_id('num1')
    num1 = num1_element.text
    num2_element = browser.find_element_by_id('num2')
    num2 = num2_element.text

    sum_num = sum(num1,num2)
    sum_num = str(sum_num)
    print('Sum1: ',sum_num)

    option = Select(browser.find_element_by_tag_name('select'))
    option.select_by_visible_text(sum_num)
    print('Option selected: ',option)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()