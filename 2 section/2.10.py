from selenium import webdriver
import math, time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/cats.html')

    button = browser.find_element_by_id('button')
    button.click()
finally:
    time.sleep(2)
    browser.quit()