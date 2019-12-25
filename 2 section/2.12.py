from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math, pyperclip

from Methods.calc import calc


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    book = browser.find_element(By.ID,'book')
    book.click()
    
    x_element = browser.find_element(By.ID,'input_value')
    x= x_element.text
    y= calc(x)
    y= str(y)

    field = browser.find_element(By.ID,'answer')
    field.send_keys(y)

    button = browser.find_element(By.ID,'solve')
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToBuffer = alert_text.split(': ')[-1]
    pyperclip.copy(addToBuffer)
    alert.accept()

finally:
    browser.quit()