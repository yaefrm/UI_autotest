from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome("../chromedriver.exe")
    browser.get(link)

    x_element = browser.find_element(By.ID, "tresure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
