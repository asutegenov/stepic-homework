from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/huge_form.html'
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_tag_name ('input')

    for element in elements:
        element.send_keys("Fuck you!")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла