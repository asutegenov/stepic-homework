import os, time, math
from selenium import webdriver



# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    first_name = browser.find_element_by_css_selector("body > .container > form > div > input[type='text']:nth-child(2)")
    first_name.send_keys('Alex')

    last_name = browser.find_element_by_xpath("//input[@name='lastname']")
    last_name.send_keys('Utegenov')

    email_form = browser.find_element_by_name('email')
    email_form.send_keys('asutegenov@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)
    
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()

finally:
    time.sleep(10)
    browser.quit()